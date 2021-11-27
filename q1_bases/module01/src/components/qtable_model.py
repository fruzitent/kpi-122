from dataclasses import dataclass

from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtSql import QSqlDatabase, QSqlRelationalDelegate, QSqlRelationalTableModel
from PySide6.QtWidgets import QTableView

from src.components.multithreading import Worker, pool
from src.utils.logger import Logger

log = Logger(__name__)


class TableSignals(QObject):
    on_update = Signal()


class DairyDelegate(QSqlRelationalDelegate):
    def __init__(self, parent, query):
        super().__init__()
        self.query = query
        self.signals = TableSignals()

    def setEditorData(self, editor, index):
        if index.column() == 0:
            editor.model().setFilter(self.query)

        return super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        self.signals.on_update.emit()
        return super().setModelData(editor, model, index)


@dataclass
class QTableModel:
    view: QTableView
    db: QSqlDatabase
    table: str
    query: str = None
    relations: list = None

    def __post_init__(self):
        self.model = self.create_model()
        self.signals = TableSignals()

    def create_model(self):
        model = QSqlRelationalTableModel(db=self.db)

        model.setTable(self.table)
        model.setFilter(self.query)

        if self.relations is not None:
            for arr in self.relations:
                model.setRelation(*arr)

        model.setSort(0, Qt.SortOrder.AscendingOrder)
        model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)

        model.select()
        return model

    def _add_row(self, args):
        row_id = self.model.rowCount()
        self.model.insertRow(row_id)

        for column, default_value in args:
            cell = self.model.index(row_id, column)
            self.model.setItemData(cell, {Qt.EditRole: default_value})

        self.view.selectRow(row_id)
        self.view.scrollToBottom()
        log.info(f"added row #{row_id} to {self.table}")

    def add_row(self, *args):
        worker = Worker(self._add_row, args)
        pool.run(worker)

    def _remove_row(self):
        row_id = self.view.currentIndex().row()

        if row_id >= 0:
            self.model.removeRow(row_id)
            self.model.select()
            self.signals.on_update.emit()
            log.info(f"removed row #{row_id} from {self.table}")

    def remove_row(self):
        worker = Worker(self._remove_row)
        pool.run(worker)
