import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class GameEngine {
	private int words_speed; // sets speed at which words travel but not respawn time
	private int words_destroyed;
	private int words_destroyed_goal;
	private boolean is_word_attacked;
	private String word_typed;
	private HashSet<Word> words_on_field; // set of all words out on the JPanel
	private HashSet<String> strings_from_file;
	private HashSet<Word> potential_words; // subset of the words on the JPanel that represent the possibilities to fire a laser at
	private HashMap<Character, Integer> dict_of_mistakes; // dictionary of letters and the number of times that the user messed up on that letter so it can be displayed at game over
	
	public GameEngine (File file) throws FileNotFoundException {
		this.words_destroyed = 0;
		this.words_speed = 2;
		this.words_destroyed_goal = 2;
		this.is_word_attacked = false;
		this.word_typed = "";
		this.strings_from_file = new HashSet<String>();
		this.words_on_field = new HashSet<Word>();
		this.potential_words = new HashSet<Word>();
		this.dict_of_mistakes = new HashMap<Character, Integer>(26);
		
		Scanner scanner = new Scanner(file);
		while(scanner.hasNext()) {
			strings_from_file.add(scanner.next().replaceAll("[^a-zA-Z]", "").toLowerCase());
		}
		scanner.close();
	}
	
	// adds word to the JPanel and words so it can be typed
	public void addWord() {
		int index = (int) ( Math.random() * strings_from_file.size() );
		String s = (String) strings_from_file.toArray()[index];
		strings_from_file.remove(s);
		Word w = new Word(s, words_speed);
		words_on_field.add(w);
		
		if (s.startsWith(word_typed)) {
			this.potential_words.add(w);
		}
		
	}
	
	private String removeWord( Word word ) {
		words_on_field.remove(word);
		potential_words = getWords();
		
		words_destroyed++;
		if( words_destroyed >= words_destroyed_goal) {
			words_speed += 1;
			words_destroyed_goal *= 5;
		}
		word_typed = "";
		is_word_attacked = false;
		return word.getWord();
	}
	
	// Checks if the string typed in the text box matches the words outside
	public String checkIfWord(char keyPressed, String word_as_is) {
		if( String.valueOf(keyPressed).matches("^[A-z]+$") ){ // if the letter typed is part of the alphabet. Makes sure that the 
			word_typed = word_as_is + keyPressed;
			for( Word w : getPotentialWords()) {
				if (w.getWord().startsWith(word_typed)) {
					is_word_attacked = true;
					if (w.getWord().equals(word_typed)) {
						return removeWord(w);
					}
				} else {
					potential_words.remove(w);
					if (word_typed.length() > 2 && w.getWord().length() > 2 && w.getWord().startsWith(word_typed.substring(0, 2))) { // checks if the word typed is an actual misspelling instead of regular typing
						addMistake(w.getWord().charAt(word_typed.length() -1));
					}
				}
			}
		} else { // if the character typed is not part of the alphabet, potential_words is reset to include all the words
			potential_words = getWords();
		}
		return null;
	}
		
	// adds a mess-up to the dictionary to display to user at game over
	private void addMistake(char c) {
		if (dict_of_mistakes.containsKey(c)) {
			int temp = dict_of_mistakes.get(c);
			temp++;
			dict_of_mistakes.put(c, temp);
		} else {
			dict_of_mistakes.put(c, 1);
		}
	}
	
	// Checks if a word box has gone off the screen
	public boolean checkOffScreen() {
		for(Word w : getWords()) {
			if (w.getX() > TypingGame.LENGTH) {
				words_on_field.remove(w);
				potential_words.remove(w);
				return true;
			}
		}
		return false;
	}
	
	public boolean isWordAttacked() {
		return is_word_attacked;
	}
	
	public void setIsWordAttacked( boolean bool) {
		is_word_attacked = bool;
	}
	public HashMap<Character, Integer> getDictionary() {
		return dict_of_mistakes;
	}
	
	// this method and the next one were made to reduce multithreading exceptions with multiple methods accessing the same data structure at the same time
	public HashSet<Word> getWords() {
		HashSet<Word> temp = new HashSet<Word>();
		temp.addAll(words_on_field);
		return temp;
	}
	
	public HashSet<Word> getPotentialWords() {
		HashSet<Word> temp = new HashSet<Word>();
		temp.addAll(potential_words);
		return temp;
	}

	public HashSet<String> getStringsFromFile() {
		return strings_from_file;
	}

}
