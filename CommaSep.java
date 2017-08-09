package scAnalytics;

import java.util.Scanner;

import com.gargoylesoftware.htmlunit.javascript.host.file.File;

public class CommaSep {

	public static void main(String[] args) {
		file input = new Scanner (new File("SC.txt"));
		String productSkus = input.nextLine();
		String newSku = "";
		String[] commSku = productSkus.split(",");
		for (int i = 0; i < 201; i++) {
			newSku = commSku[i];
			System.out.println(commSku);

		}
	}
}
