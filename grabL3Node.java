package parts;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class grabL3Node {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner input1 = new Scanner(new File("ga.csv"));
		Scanner input2 = new Scanner(new File("EDII.csv"));

		while (input2.hasNextLine()) {
			String line = input2.nextLine();
			String[] lineSplit = line.split(",");
			String[][] lineArray = new String[133][1];
			for (int i = 0; i < 1; i++) {
				lineArray[i][0] = lineSplit[i];
				while (i < 1 && input1.hasNextLine()) {
					String line1 = input1.nextLine();
					String[] line1Split = line1.split(",");
					String[][] line1Array = new String[52616][2];
					for (int j = 0; j < 1; j++) {
						line1Array[j][0] = line1Split[j];
						for (int k = 1; k < 2; k++) {
							line1Array[j][k] = line1Split[k];
						}
						if (lineArray[i][0].equals(line1Array[j][0])) {
							System.out.println(line1Array[j][0] + ", " + line1Array[j][1]);
							i += 1;
						}
						
					}
				}

			}
		}

	}
}
