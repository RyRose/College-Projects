import java.awt.Graphics;
import java.awt.Color;
import java.awt.Font;

public class Word {
	private int x; private int y; //at top left
	private int width; private int height;
	private int speed;
	private String word;
	private Color bkgrd_color;
	private Color word_color;
	private Font font;
	
	public Word(String word, int speed) {
		this.word = word;
		this.width = word.length()*9;
		this.height = 20;
		this.x = -width;
		this.y = (int) (Math.random() * (TypingGame.HEIGHT - 100)) + height;
		this.speed = speed;
		this.bkgrd_color = Color.magenta;
		this.word_color = Color.YELLOW;
		this.font = new Font("Monospaced", Font.BOLD, 14);
		
	}
	
	public void draw(Graphics g) {
		Color c = g.getColor();
		Font f = g.getFont();
		
		g.setColor(bkgrd_color);
		g.fillRect(x, y, width, height);
		
		g.setColor(word_color);
		g.setFont(font);
		g.drawString(word, x+3, y+15);
		
		g.setColor(c);
		g.setFont(f);
		
		move();		
	}
	
	private void move() {
		this.x += speed;
	}
	
	public int getX() {
		return x;
	}
	
	public int [] getPos() {
		int [] array = { x + width/2, y + height/2 };
		return array;
	}
	
	public String getWord() {
		return word;
	}
	
}
