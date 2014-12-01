import javax.swing.*;

import java.awt.event.*;
import java.awt.*;

public class Typing extends JFrame implements ActionListener, KeyListener {
	private GameEngine engine;
	private DrawPane canvas;
	private JSlider slider;
	private Timer timer;
	
	public Typing() {
		super("Typing");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(1024,768);
		engine = new GameEngine();
		canvas = new DrawPane();
		getContentPane().setLayout(new BorderLayout());
		getContentPane().add(canvas);
        Insets insets = this.getInsets();
        canvas.setSize(this.getWidth() - insets.left - insets.right, this.getHeight()- insets.top - insets.bottom );
        canvas.setLocation(insets.left,insets.top);
        canvas.setBackground(Color.WHITE);
        timer = new Timer(150, this);
        timer.start();
	}
	
	public void keyPressed (KeyEvent ke) {}
	public void keyTyped(KeyEvent ke) {}
	public void keyReleased(KeyEvent ke) {}
	public void actionPerformed(ActionEvent ae) {
		if (ae.getSource() == timer) {
			engine.addWord();
		}
	}
	
	public void paintCanvas(Graphics g) {
		for(Word word : engine.getList()) {
			word.draw(g);
		}
		
		
	}
	
	public static void main(String[] args) {
		Typing game = new Typing();
		game.setVisible(true);
	}
}
