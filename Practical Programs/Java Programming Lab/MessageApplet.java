// import java.applet.Applet;
// import java.awt.Graphics;

// public class MessageApplet extends Applet {

//     public void paint(Graphics g) {
//         g.drawString("Hello! Welcome to Java Applets.", 50, 100);
//     }
// }


import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class MessageApplet extends Frame {

    MessageApplet() {
        setTitle("Simple Java Message");
        setSize(400, 200);
        setVisible(true);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                dispose();
            }
        });
    }

    public void paint(Graphics g) {
        super.paint(g);
        g.drawString("Hello! Welcome to Java Applets.", 100, 100);
    }

    public static void main(String[] args) {
        new MessageApplet();
    }
}