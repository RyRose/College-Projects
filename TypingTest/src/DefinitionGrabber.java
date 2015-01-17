import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class DefinitionGrabber {
	
	public static String define(String word) {
		URL url;
		InputStream input_stream;
		URLConnection connection;
		try {
	        url = new URL("http://www.dictionary.reference.com/browse/" + word);
	        connection = url.openConnection();
	        input_stream =connection.getInputStream();
	    } catch (MalformedURLException e) {
	    	return word + " is not found since " + word + " carries invalid characters.";
	    } catch (IOException e) {
	    	return word + " is not found since Dictionary.com is down or your internet is off. Please try again.";
	    }
		
		String line = "";
		Scanner scanner = new Scanner(new InputStreamReader(input_stream));
		for(int i = 0; i < 232; i++) {
			line = scanner.nextLine();
		}
		if (!line.contains("English dictionary,") && !line.contains("Dictionary.com")) {
     	   	return word + ": " + line.substring(line.indexOf(",") + 1, line.indexOf(".") +1);
		}
		return word + " not found.";
	}
	
}
