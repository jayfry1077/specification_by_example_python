Feature: reversing json data

  Scenario Outline: reverse some simple json
     Given we have <input>
      When we reverse that data
      Then it should look like <output>

      Examples: Input Variables
        | input              |output|
        |{"name": "Jonathan"}| {"Jonathan": "name"}|
