package adobeTaxonomy;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class trailCom {

	public static void main(String[] args) {
		try {
			BufferedReader input = new BufferedReader(new FileReader("TrailingComma.txt"));
			String line = "";
			
			while ((line = input.readLine()) != null) {
				if (line.endsWith(",")) {
					line = line.substring(0, line.length() - 1);

					System.out.print(line);
				} else {
					System.out.print(line);
				}
				System.out.println();
				
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
