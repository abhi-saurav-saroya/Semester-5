
import java.awt.*;
import java.awt.event.*;

public class MouseEventDemo extends Frame {
    Label label;

    MouseEventDemo() {
        label = new Label("Perform a mouse event", Label.CENTER);
        add(label);

        label.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                label.setText("Mouse Clicked");
            }

            public void mousePressed(MouseEvent e) {
                label.setText("Mouse Pressed");
            }

            public void mouseReleased(MouseEvent e) {
                label.setText("Mouse Released");
            }

            public void mouseEntered(MouseEvent e) {
                label.setText("Mouse Entered");
            }

            public void mouseExited(MouseEvent e) {
                label.setText("Mouse Exited");
            }
        });

        label.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseMoved(MouseEvent e) {
                label.setText("Mouse Moved");
            }

            public void mouseDragged(MouseEvent e) {
                label.setText("Mouse Dragged");
            }
        });

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                dispose();
            }
        });

        setTitle("Mouse Events");
        setSize(250, 150);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    public static void main(String[] args) {
        new MouseEventDemo();
    }
}