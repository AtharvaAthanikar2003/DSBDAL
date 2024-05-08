object Calculator {
  def main(args: Array[String]): Unit = {
    println("Welcome to Scala Calculator")
    println("Enter an expression (e.g., 2 + 2) or type 'exit' to quit:")

    var continue = true
    while (continue) {
      val input = scala.io.StdIn.readLine()

      if (input.toLowerCase == "exit") {
        println("Exiting...")
        continue = false
      } else {
        try {
          val result = evaluate(input)
          println(s"Result: $result")
        } catch {
          case e: Exception =>
            println(s"Error: ${e.getMessage}")
        }
      }
    }
  }

  def evaluate(expression: String): Double = {
    val parts = expression.split("")
    if (parts.length != 3)
      throw new IllegalArgumentException("Invalid expression format")

    val num1 = parts(0).toDouble
    val operator = parts(1)
    val num2 = parts(2).toDouble

    operator match {
      case "+" => num1 + num2
      case "-" => num1 - num2
      case "*" => num1 * num2
      case "/" =>
        if (num2 == 0)
          throw new ArithmeticException("Division by zero")
        else
          num1 / num2
      case _ => throw new IllegalArgumentException("Unsupported operator")
    }
  }
}


