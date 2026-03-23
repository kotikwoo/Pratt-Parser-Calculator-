# EN Pratt-Parser-Calculator

A simple math interpreter built from scratch in Python using a **Pratt parser**.

This project evaluates basic mathematical expressions and is useful for learning how computers process human-readable input. It is also a good first step toward building a programming language, data language, or other custom syntax-based system.

## Overview

The calculator processes user input in three main stages:

1. **Lexing**
2. **Parsing**
3. **Interpreting**

Each stage has its own role in understanding and evaluating mathematical expressions.

## Lexer

The **lexer** reads the raw input and breaks it into smaller pieces called **tokens**. It also identifies the type of each token.

For example, the input:

`12 + 24`

is converted into:

`NUMBER:12`, `PLUS`, `NUMBER:24`

Whitespace is usually ignored during this stage.

## Parser

The **parser** analyzes the sequence of tokens and determines how the expression should be structured.

This project uses a **Pratt parser written from scratch**. A Pratt parser is especially useful for mathematical expressions because it handles **operator precedence** and **associativity** in a clean and flexible way.

For example, if an expression contains both addition and multiplication, the parser correctly determines that multiplication should be evaluated first.

The parser then builds a tree-like structure representing the expression.

## Interpreter

The **interpreter** evaluates the structure created by the parser and performs the required mathematical operations.

It contains the logic for handling operations such as:

- Addition
- Subtraction
- Multiplication
- Division
- Unary plus
- Unary minus

## Why This Project Is Useful

This project helps demonstrate:

- how raw text input is tokenized
- how expressions are parsed into a structured form
- how parsed expressions are evaluated
- how a simple interpreter can be built from scratch

It can also serve as a foundation for more advanced projects such as a compiler, transpiler, or full programming language.

## Example

Input:

`5 + 3 * 2`

Output:

`11`

## Technologies Used

- Python
- Pratt Parser
- Object-Oriented Design

# RU Pratt-Parser-Calculator

Простой математический интерпретатор, написанный с нуля на Python с использованием **Pratt parser**.

Этот проект вычисляет базовые математические выражения и помогает понять, как компьютер обрабатывает текст, введённый человеком. Также он может стать хорошим первым шагом к созданию собственного языка программирования, языка запросов или другой системы со своей логикой и синтаксисом.

## Обзор

Калькулятор обрабатывает пользовательский ввод в три основных этапа:

1. **Лексический анализ**
2. **Синтаксический анализ**
3. **Интерпретация**

Каждый из этих этапов выполняет свою задачу при разборе и вычислении математического выражения.

## Лексер

**Лексер** считывает исходный ввод и разбивает его на более мелкие части, которые называются **токенами**. Также он определяет тип каждого токена.

Например, ввод:

`12 + 24`

преобразуется в:

`NUMBER:12`, `PLUS`, `NUMBER:24`

Пробелы на этом этапе обычно игнорируются.

## Парсер

**Парсер** анализирует последовательность токенов и определяет, как именно должно быть устроено выражение.

В этом проекте используется **Pratt parser, реализованный с нуля**. Такой способ разбора особенно удобен для математических выражений, потому что он позволяет корректно учитывать **приоритет операторов** и их **ассоциативность**.

Например, если в выражении есть и сложение, и умножение, парсер правильно определит, что умножение должно выполняться раньше сложения.

После этого парсер строит древовидную структуру, которая представляет выражение.

## Интерпретатор

**Интерпретатор** вычисляет структуру, созданную парсером, и выполняет нужные математические операции.

Он содержит логику для таких операций, как:

- Сложение
- Вычитание
- Умножение
- Деление
- Унарный плюс
- Унарный минус

## Почему этот проект полезен

Этот проект помогает понять:

- как текстовый ввод разбивается на токены
- как выражения преобразуются в структурированную форму
- как эта структура затем вычисляется
- как можно создать простой интерпретатор с нуля

Также этот проект может стать основой для более сложных систем, например компилятора, транспайлера или полноценного языка программирования.

## Пример

Ввод:

`5 + 3 * 2`

Результат:

`11`

## Используемые технологии

- Python
- Pratt Parser
- Объектно-ориентированный подход
