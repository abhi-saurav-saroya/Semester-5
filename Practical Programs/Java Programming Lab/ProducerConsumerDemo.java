class SharedBuffer {
    int item;
    boolean available = false;

    synchronized void produce(int value) {
        try {
            while (available) {
                wait();
            }

            item = value;
            System.out.println("Produced: " + item);

            available = true;
            notify();

        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }

    synchronized void consume() {
        try {
            while (!available) {
                wait();
            }

            System.out.println("Consumed: " + item);

            available = false;
            notify();

        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }
}

class Producer extends Thread {
    SharedBuffer buffer;

    Producer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    public void run() {
        int value = 1;

        while (true) {
            buffer.produce(value++);
            
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

class Consumer extends Thread {
    SharedBuffer buffer;

    Consumer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    public void run() {
        while (true) {
            buffer.consume();

            try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

public class ProducerConsumerDemo {
    public static void main(String[] args) {
        SharedBuffer buffer = new SharedBuffer();

        Producer producer = new Producer(buffer);
        Consumer consumer = new Consumer(buffer);

        producer.start();
        consumer.start();
    }
}
