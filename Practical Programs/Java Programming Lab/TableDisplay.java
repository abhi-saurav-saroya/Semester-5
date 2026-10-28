import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class TableDisplay extends Frame {
    TableDisplay() {
        setTitle("Table Display");
        setLayout(new GridLayout(0, 1));

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                dispose();
            }
        });

        try {
            BufferedReader br = new BufferedReader(
                new FileReader("Table.txt")
            );

            String line;
            while ((line = br.readLine()) != null) {
                String[] data = line.split(",");

                Panel row = new Panel(new GridLayout(1, data.length));

                for (String value : data) {
                    row.add(new Label(value.trim(), Label.CENTER));
                }

                add(row);
            }

            br.close();
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }

        setSize(500, 300);
        setVisible(true);
    }

    public static void main(String[] args) {
        new TableDisplay();
    }
}
