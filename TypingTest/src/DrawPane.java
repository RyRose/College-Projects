import java.awt.Graphics;
import javax.swing.JPanel;

public class DrawPane extends JPanel {
		Typing game;
	
	public void paintComponent(Graphics g) {
        super.paintComponent(g);
        game.paintCanvas(g);
    }
}
