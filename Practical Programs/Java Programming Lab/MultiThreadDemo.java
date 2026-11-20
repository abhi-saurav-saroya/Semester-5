import java.util.Random;

class NumberGenerator extends Thread {
    public void run() {
        Random random = new Random();

        try {
            while (true) {
                int num = random.nextInt(100);

                System.out.println("\nGenerated Number: " + num);

                if (num % 2 == 0) {
                    new EvenThread(num).start();
                } else {
                    new OddThread(num).start();
                }

                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Generator interrupted.");
        }
    }
}

class EvenThread extends Thread {
    int num;

    EvenThread(int num) {
        this.num = num;
    }

    public void run() {
        System.out.println("Square: " + (num * num));
    }
}

class OddThread extends Thread {
    int num;

    OddThread(int num) {
        this.num = num;
    }

    public void run() {
        System.out.println("Cube: " + (num * num * num));
    }
}

public class MultiThreadDemo {
    public static void main(String[] args) {
        new NumberGenerator().start();
    }
}
