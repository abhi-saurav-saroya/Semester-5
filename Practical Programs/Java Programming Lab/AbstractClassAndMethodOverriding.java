abstract class Shape {
    int a, b;
    abstract void printArea();
}

class Rectangle extends Shape{
    void printArea() {
        System.out.println("Area of Rectangle = " + (a * b));
    }
}

class Triangle extends Shape {
    void printArea() {
        System.out.println("Area of Triangle = " + (0.5 * a * b));
    }
}

class Circle extends Shape {
    void printArea() {
        System.out.println("Area of Circle = " + (3.14 * a * a));
    }
}

public class AbstractClassAndMethodOverriding {
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle();
        rectangle.a = 10;
        rectangle.b = 5;

        Triangle triangle = new Triangle();
        triangle.a = 7;
        triangle.b = 9;

        Circle circle = new Circle();
        circle.a = 15;

        rectangle.printArea();
        triangle.printArea();
        circle.printArea();
    }
}