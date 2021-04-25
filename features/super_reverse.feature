Feature: reverse a json with super_json_reverser

  Scenario Outline: reverse some simple json data with our super_json_reverser
     Given <input_data> for our super_json_reverser
      When we call our super_json_reverser function
      Then we should get the following <output_data>

      Examples: Input Variables for super reverser
        | input_data     |output_data|
        |{"name": "John"}| {"John": "name"}|