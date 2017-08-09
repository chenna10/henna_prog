package parts;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class format {
	
	public static void main (String [] args) throws IOException {
		
		try {
			BufferedReader file1 = new BufferedReader(new FileReader("IWE.csv"));
			
			BufferedReader file2 = new BufferedReader(new FileReader("imageNA.txt"));
			String [] lineArray = new String [500000];
			while (file2.ready()) {
				String line = file2.readLine();
				String [] array = line.split(",");
				String [][] newArray = new String [62520][1];
				for (int i = 0; i < array.length ; i++) {
					for (int j = 0; j < 1; j++) {
						newArray[i][j] = array[i];
						lineArray [i] = newArray[i][j];
						String s1 = lineArray[i];
//						if (lineArray[i].contains("[")) {
//							lineArray[i] = lineArray[i].replace("[", "" );
//						}
//						if (lineArray[i].contains("]")) {
//							lineArray[i] = lineArray[i].replace("]", "");
//						}
//						if (lineArray[i].contains(":")) {
//							lineArray[i] = lineArray[i].replaceAll(":", "");
//						}
//						lineArray[i] = lineArray[i].replaceAll("/", "");
//						lineArray[i] = lineArray[i].replaceAll(" ", "");
						
						if (s1.contains("?")) {
							s1 = s1.substring(0, s1.indexOf("?"));
						}
						System.out.println(s1);
					}
				}
			}
			file1.close();
			file2.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

}
