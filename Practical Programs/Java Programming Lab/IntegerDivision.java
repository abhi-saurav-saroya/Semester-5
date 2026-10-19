import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class IntegerDivision implements ActionListener {
    TextField num1TextField, num2TextField, resultTextField;
    Panel inputPanel, buttonPanel;
    Button integerDivision, equalsTo;
    int num1, num2, result;
    Frame frame;

    public IntegerDivision() {
        frame = new Frame("Integer Division");
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                frame.dispose();
                System.exit(0);
            }
        });

        inputPanel = new Panel();
        inputPanel.setLayout(new GridLayout(1, 3));

        num1TextField = new TextField();
        num1TextField.setFont(new Font("Arial", Font.BOLD, 25));
        inputPanel.add(num1TextField);

        integerDivision = new Button("//");
        inputPanel.add(integerDivision);
        integerDivision.addActionListener(this);

        num2TextField = new TextField();
        num2TextField.setFont(new Font("Arial", Font.BOLD, 25));
        inputPanel.add(num2TextField);

        frame.add(inputPanel, BorderLayout.NORTH);

        buttonPanel = new Panel(new FlowLayout(FlowLayout.CENTER));
        equalsTo = new Button("=");
        equalsTo.setFont(new Font("Arial", Font.BOLD, 20));
        equalsTo.setPreferredSize(new Dimension(80, 40));
        buttonPanel.add(equalsTo);
        frame.add(buttonPanel, BorderLayout.CENTER);
        equalsTo.addActionListener(this);

        resultTextField = new TextField();
        resultTextField.setEditable(false);
        resultTextField.setFont(new Font("Arial", Font.BOLD, 25));
        frame.add(resultTextField, BorderLayout.SOUTH);

        frame.setSize(400, 170);
        frame.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if (command.equals("=")) {
            try {
                num1 = Integer.parseInt(num1TextField.getText().trim());
                num2 = Integer.parseInt(num2TextField.getText().trim());

                if (num2 == 0) {
                    throw new ArithmeticException(
                        "Cannot Divide by Zero."
                    );
                }

                result = num1 / num2;
                resultTextField.setText(String.valueOf(result));

            } catch (ArithmeticException ex) {
                JOptionPane.showMessageDialog(
                    frame,
                    ex.getMessage(),
                    "Arithmetic Error",
                    JOptionPane.ERROR_MESSAGE
                );
                resultTextField.setText("");

            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(
                    frame,
                    "Please enter valid integers.",
                    "Input Error",
                    JOptionPane.ERROR_MESSAGE
                );
                resultTextField.setText("");
            }
        }
    }

    public static void main(String[] args) {
        new IntegerDivision();
    }
}