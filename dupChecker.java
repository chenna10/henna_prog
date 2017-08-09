package parts;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class dupChecker {

	public static void main(String[] args) throws IOException {
		Scanner input1 = new Scanner(new File("ga.txt"));
		Scanner input2 = new Scanner(new File("IEI.txt"));
		
		ArrayList<String> itemList = new ArrayList<String>();
		ArrayList<String> checkList = new ArrayList<String>();
		
		while(input1.hasNext()) {
			itemList.add(input1.next());
		}
		while(input2.hasNext()) {
			checkList.add(input2.next());
		}
		List<String> union = new ArrayList<String>(itemList);
		union.addAll(checkList);
		
		List<String> intersection = new ArrayList<String>(itemList);
		intersection.retainAll(checkList);
		
		List<String> notIn = new ArrayList<String>(checkList);
		notIn.removeAll(itemList);
		
		List<String> symDif = new ArrayList(union);
		symDif.removeAll(intersection);
		
//		System.out.println("item: " + itemList);
//		System.out.println("check: " + checkList);
//		System.out.println("Union: " + union);
		System.out.println("Intersection: " + intersection);
		//System.out.println("Parts in New JSON but not in Codify tax:" + notIn);
	}
}