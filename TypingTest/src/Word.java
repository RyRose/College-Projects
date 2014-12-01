import java.awt.Graphics;
public class Word {
	private String word;
	private int x;
	private int y;
	
	public Word(String word, int y) {
		this.word = word.toLowerCase().trim();
		x = -40;
		this.y= y;
	}
	
	public String getWord() {
		return word;
	}
	
	public int getScore() {
		return word.length();
	}
	
	public void draw(Graphics g) {
		g.drawString(word, x, y);
	}
	
	public void move() {
		x += 4;
	}
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}
}
