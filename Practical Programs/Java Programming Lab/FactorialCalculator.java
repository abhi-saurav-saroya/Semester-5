
// import java.applet.Applet;
// import java.awt.*;
// import java.awt.event.*;
// import java.math.BigInteger;

// public class FactorialApplet extends Applet implements ActionListener {
//     TextField input, output;
//     Button compute;

//     public void init() {
//         setLayout(new GridLayout(3, 2, 5, 5));

//         add(new Label("Enter an integer:"));
//         input = new TextField();
//         add(input);

//         add(new Label("Factorial:"));
//         output = new TextField();
//         output.setEditable(false);
//         add(output);

//         compute = new Button("Compute");
//         add(compute);

//         add(new Label(""));

//         compute.addActionListener(this);
//     }

//     public void actionPerformed(ActionEvent e) {
//         try {
//             int n = Integer.parseInt(input.getText().trim());

//             if (n < 0) {
//                 output.setText("Enter non-negative integer");
//                 return;
//             }

//             BigInteger fact = BigInteger.ONE;

//             for (int i = 1; i <= n; i++) {
//                 fact = fact.multiply(BigInteger.valueOf(i));
//             }

//             output.setText(fact.toString());

//         } catch (NumberFormatException ex) {
//             output.setText("Invalid integer");
//         }
//     }
// }



import java.awt.*;
import java.awt.event.*;
import java.math.BigInteger;

public class FactorialCalculator extends Frame implements ActionListener {
    TextField input, output;
    Button compute;

    FactorialCalculator() {
        setTitle("Factorial Calculator");
        setSize(400, 180);
        setLayout(new GridLayout(3, 2, 5, 5));

        add(new Label("Enter an integer:"));
        input = new TextField();
        add(input);

        add(new Label("Factorial:"));
        output = new TextField();
        output.setEditable(false);
        add(output);

        compute = new Button("Compute");
        add(compute);

        add(new Label(""));

        compute.addActionListener(this);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                dispose();
            }
        });

        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        try {
            int n = Integer.parseInt(input.getText().trim());

            if (n < 0) {
                output.setText("Enter non-negative integer");
                return;
            }

            BigInteger fact = BigInteger.ONE;

            for (int i = 1; i <= n; i++) {
                fact = fact.multiply(BigInteger.valueOf(i));
            }

            output.setText(fact.toString());

        } catch (NumberFormatException ex) {
            output.setText("Invalid integer");
        }
    }

    public static void main(String[] args) {
        new FactorialCalculator();
    }
}
