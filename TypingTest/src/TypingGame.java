import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenuBar;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.Timer;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.File;
import java.io.FileNotFoundException;

@SuppressWarnings("serial")
public class TypingGame extends JFrame implements ActionListener, KeyListener {
	public final static int HEIGHT = 624; public final static int LENGTH = 1200;
	private int lives;
	private int score;
	private int spawn_time; // time between spawning new words
	private boolean game_over;
	private boolean is_game_paused; // boolean condition of whether the game is paused or not
	private String destroyed_word; // null if no words destroyed, else, it is the name of the word that was destroyed
	private GameEngine engine;
	private JPanel canvas;
	private JLabel score_number_label;
	private JLabel lives_number_label;
	private JTextField definition_text_field;
	private JTextField typing_text_field;
	private JButton play_pause_button;
	private Timer draw_timer;
	private Timer word_spawn_timer;

	public TypingGame(File file) throws FileNotFoundException{
		this.spawn_time = 5000; // in milliseconds
		this.score = 0;
		this.lives = 3;
		this.game_over = false;
		this.is_game_paused = false;
		this.destroyed_word = null;
		this.engine = new GameEngine(file);
		this.draw_timer = new Timer(100,this);
		this.word_spawn_timer = new Timer( spawn_time, this);
		
		setTitle("Typing Game");
		setSize(1200,700);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		getContentPane().setLayout(new BorderLayout());
		
		//setting up the drawing panel
		this.canvas = new JPanel() {
			public void paintComponent(Graphics g) {
				super.paintComponent(g);
				TypingGame.this.paintEverything(g);
			}
		};       
		canvas.setBackground(Color.black);
		getContentPane().add(canvas, BorderLayout.CENTER);
		
		
		//setting up the JMenuBar at the top
		JMenuBar top_bar = new JMenuBar();
		JLabel lives_label = new JLabel("   Lives: ");
		JLabel score_label = new JLabel("Score: ");
		this.lives_number_label = new JLabel("3");
		this.definition_text_field = new JTextField("Definition:");
		this.definition_text_field.setEditable(false);
		this.score_number_label = new JLabel("0");
		top_bar.add(lives_label);
		top_bar.add(lives_number_label);
		top_bar.add(new JLabel("      "));
		top_bar.add(score_label);
		top_bar.add(score_number_label);
		top_bar.add(new JLabel("    "));
		top_bar.add(definition_text_field);
		getContentPane().add(top_bar, BorderLayout.NORTH);
		
		// setting up the JMenuBar at the bottom
		JMenuBar bottom_bar = new JMenuBar();
		this.play_pause_button = new JButton("Play/Pause");
		play_pause_button.addActionListener(this);
		this.typing_text_field = new JTextField();
		typing_text_field.addKeyListener(this);
		bottom_bar.add(play_pause_button);
		bottom_bar.add(typing_text_field);
		getContentPane().add(bottom_bar, BorderLayout.SOUTH);
		
		engine.addWord();	
		draw_timer.start();
		word_spawn_timer.start();
	}
	
	public void actionPerformed( ActionEvent ae ) {
		if (!game_over) {
			if (destroyed_word != null) { 
				score += 100;
				spawn_time -= 20;
				score_number_label.setText(String.valueOf(score));
				typing_text_field.setText(""); // clears the the typing_text_field
				definition_text_field.setText("Definition of " + DefinitionGrabber.define(destroyed_word));
				word_spawn_timer.setDelay(spawn_time);
				if (engine.getStringsFromFile().isEmpty()) {
					game_over = true;
				}
				destroyed_word = null;
			}
			
			if (ae.getSource() == draw_timer && !is_game_paused) {
				canvas.repaint();
			} else if (ae.getSource() == word_spawn_timer && !is_game_paused) {
				engine.addWord();
			} else if (ae.getSource() == play_pause_button) {
				if (is_game_paused) {
					typing_text_field.setEditable(true);
					is_game_paused = false;
				} else {
					typing_text_field.setEditable(false);
					is_game_paused = true;
				}
			}
			
			if (engine.checkOffScreen()) {
				if(lives == 0) {
					game_over = true;
				} else {
					lives -= 1;
					spawn_time += 200;
				}
				lives_number_label.setText(lives + "");
			}
		} else {
			canvas.repaint();
		}
	}
	
	
	private void paintEverything(Graphics g) {
		if( game_over ) {
			drawKillScreen(g);
		} else {
			if (engine.isWordAttacked()) { 
				Color c = g.getColor();
				g.setColor(Color.RED);
				for( Word w : engine.getPotentialWords()) {
					g.drawLine(w.getPos()[0], w.getPos()[1], 500, 700);
				}
				g.setColor(c);
				engine.setIsWordAttacked(false);
			}
			
			for( Word i : engine.getWords()) {
				i.draw(g);
			}
		}
	}
	
	private void drawKillScreen(Graphics g) {
		word_spawn_timer.stop();
		draw_timer.stop();
		typing_text_field.setEditable(false);
		g.setColor(Color.white);
		g.drawString("Game Over!", 580, 20);
		g.drawString("You have a score of " + score, 550, 40);
		g.drawString("Here are letters you need to work on:", 510, 60);
		g.drawString("Letters : Number of mistakes", 540, 80);
		int y = 110;
		for ( char a : engine.getDictionary().keySet()) {
			g.drawString(a + " : " + engine.getDictionary().get(a), 600, y);
			y += 20;
		}
	}
	
	public void keyPressed(KeyEvent ke) {
		if (!game_over && !is_game_paused) {
			this.destroyed_word = engine.checkIfWord(ke.getKeyChar(), typing_text_field.getText());
		}
	}
	public void keyTyped(KeyEvent ke) {} 
	public void keyReleased(KeyEvent ke) {}
	
	public static void main(String args[]) {
		String input = null;
		String error = " :";
		while(input == null) {
			input = JOptionPane.showInputDialog("Enter file name (words.txt exists in the main directory)" + error);
			try {
				new TypingGame(new File(input)).setVisible(true);
			} catch (FileNotFoundException e) {
				input = null;
				error = ". File does not exist, try again:";
			}
		}	
	}
}
