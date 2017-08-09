package parts;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part_url_check {
	
	public static void main (String [] args) throws FileNotFoundException {
		Scanner input1 = new Scanner(new File("ga.txt"));
		Scanner input2 = new Scanner(new File("iwe_url.txt"));
		
		while (input2.hasNextLine()) {
			String line = input2.nextLine();
			String[] lineSplit = line.split(",");
			String[][] lineArray = new String[61290][1];
			for (int i = 0; i < 1; i++) {
				lineArray[i][0] = lineSplit[i];
				while (i < 1 && input1.hasNextLine()) {
					String line1 = input1.nextLine();
					line1 = line1.toLowerCase();
					String[] line1Split = line1.split(",");
					String[][] line1Array = new String[62520][1];
					for (int j = 0; j < 1; j++) {
						line1Array[j][0] = line1Split[j];
						if (lineArray[i][0].contains(line1Array[j][0])) {
							System.out.println(lineArray[i][0]);
							i+=1;
						}
					}
				}

			}
		}
	}
}
