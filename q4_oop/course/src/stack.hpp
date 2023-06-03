#ifndef MYPROJECT_STACK_HPP_
#define MYPROJECT_STACK_HPP_

#include "./io.hpp"
#include "./vector.hpp"

#include <cstddef>
#include <iosfwd>
#include <sstream>
#include <type_traits>
#include <utility>
#include <variant>

namespace myproject {
    template <typename Contained, typename Container = vector<Contained>>
    class stack {
      public:
        using container_type = Container;

        using value_type      = typename container_type::value_type;
        using reference       = typename container_type::reference;
        using const_reference = typename container_type::const_reference;
        using size_type       = typename container_type::size_type;

        static_assert(std::is_same_v<Contained, value_type>);

      protected:
        container_type _container;

      public:
        constexpr stack() requires std::is_default_constructible_v<Container> : _container() {}

        explicit constexpr stack(const Container &container) : _container(container) {}

        explicit constexpr stack(Container &&container) : _container(std::move(container)) {}

        template <typename Allocator>
        requires std::uses_allocator_v<Container, Allocator>
        explicit constexpr stack(const Allocator &allocator) : _container(allocator) {}

        template <typename Allocator>
        requires std::uses_allocator_v<Container, Allocator>
        constexpr stack(const Container &container, const Allocator &allocator) : _container(container, allocator) {}

        template <typename Allocator>
        requires std::uses_allocator_v<Container, Allocator>
        constexpr stack(const stack &other, const Allocator &allocator) : _container(other._container, allocator) {}

        template <typename Allocator>
        requires std::uses_allocator_v<Container, Allocator>
        constexpr stack(Container &&container, const Allocator &allocator) :
            _container(std::move(container), allocator) {}

        template <typename Allocator>
        requires std::uses_allocator_v<Container, Allocator>
        constexpr stack(stack &&other, const Allocator &allocator) :
            _container(std::move(other._container), allocator) {}

        constexpr auto emplace(auto &&...args) -> reference {
            return _container.emplace_back(std::forward<decltype(args)>(args)...);
        }

        [[nodiscard]] constexpr auto empty() const -> bool {
            return _container.empty();
        }

        constexpr auto pop() -> void {
            _container.pop_back();
        }

        constexpr auto push(const value_type &value) -> void {
            _container.push_back(value);
        }

        constexpr auto push(value_type &&value) -> void {
            _container.push_back(std::move(value));
        }

        [[nodiscard]] constexpr auto size() const -> size_type {
            return _container.size();
        }

        constexpr auto swap(stack &other) noexcept(std::is_nothrow_swappable_v<Container>) -> void {
            using std::swap;
            swap(_container, other._container);
        }

        [[nodiscard]] constexpr auto top() -> reference {
            return _container.back();
        }

        [[nodiscard]] constexpr auto top() const -> const_reference {
            return _container.back();
        }
    };
} // namespace myproject

namespace myproject {
    template <typename Contained, typename Container>
    constexpr auto erase(stack<Contained, Container> *stack) -> void {
        std::remove_pointer_t<decltype(stack)> temp;
        stack->swap(temp);
    }

    template <typename Contained, typename Container>
    constexpr auto for_each(stack<Contained, Container> *stack, auto &&callback) -> void {
        while (!stack->empty()) {
            callback(stack->top());
            stack->pop();
        }
    }

    template <typename Contained, typename Container>
    constexpr auto for_each(const stack<Contained, Container> &stack, auto &&callback) -> void {
        auto copy = stack;
        for_each(&copy, std::forward<decltype(callback)>(callback));
    }

    template <typename Contained, typename Container>
    constexpr auto reverse(stack<Contained, Container> *stack) noexcept -> void {
        if (stack->empty()) {
            return;
        }

        std::remove_pointer_t<decltype(stack)> tmp;

        while (!stack->empty()) {
            tmp.push(stack->top());
            stack->pop();
        }

        stack->swap(tmp);
    }

    template <typename Contained, typename Container>
    constexpr auto merge(stack<Contained, Container> *lhs,
                         stack<Contained, Container> *rhs,
                         stack<Contained, Container> *stack,
                         auto                       &&predicate) -> void {
        std::remove_pointer_t<decltype(stack)> merged;

        while (!lhs->empty() && !rhs->empty()) {
            if (predicate(lhs->top(), rhs->top())) {
                merged.push(lhs->top());
                lhs->pop();
            } else {
                merged.push(rhs->top());
                rhs->pop();
            }
        }

        while (!lhs->empty()) {
            merged.push(lhs->top());
            lhs->pop();
        }

        while (!rhs->empty()) {
            merged.push(rhs->top());
            rhs->pop();
        }

        while (!merged.empty()) {
            stack->push((merged.top()));
            merged.pop();
        }
    }

    template <typename Contained, typename Container>
    constexpr auto sort(stack<Contained, Container> *stack, auto &&predicate) -> void {
        std::remove_pointer_t<decltype(stack)> lhs;
        std::remove_pointer_t<decltype(stack)> rhs;

        while (!stack->empty()) {
            if (stack->size() % 2 == 0) {
                lhs.push(stack->top());
            } else {
                rhs.push(stack->top());
            }
            stack->pop();
        }

        if (lhs.size() > 1) {
            sort(&lhs, predicate);
        }

        if (rhs.size() > 1) {
            sort(&rhs, predicate);
        }

        merge(&lhs, &rhs, stack, predicate);
    }
} // namespace myproject

namespace myproject {
    template <typename Contained, typename Container>
    constexpr auto read(std::istream &is, stack<Contained, Container> *obj) noexcept -> void {
        using size_type = typename std::remove_pointer_t<decltype(obj)>::size_type;

        size_type size{};
        read(is, &size);

        using detail::read;
        for (std::size_t i = 0; i < size; ++i) {
            Contained value{};
            read(is, &value);
            obj->push(value);
        }

        reverse(obj);
    }

    template <typename Contained, typename Container>
    constexpr auto write(std::ostream &os, const stack<Contained, Container> &obj) noexcept -> void {
        write(os, obj.size());
        for_each(obj, [&os](const auto &value) {
            write(os, value);
        });
    }
} // namespace myproject

#endif // MYPROJECT_STACK_HPP_
