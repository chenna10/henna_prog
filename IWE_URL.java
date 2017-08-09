package parts;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class IWE_URL {

	public static void main(String[] args) throws FileNotFoundException {

		Scanner input1 = new Scanner(new File("IWE_tax.csv"));
		ArrayList<String> iweList = new ArrayList<String>();
		Scanner input2 = new Scanner(new File("EDI.csv"));
		ArrayList<String> ediList = new ArrayList<String>();

		while (input1.hasNextLine()) {
			iweList.add(input1.nextLine());
		}

		while (input2.hasNextLine()) {
			ediList.add(input2.nextLine());
		}

		String[] iweArray = new String[iweList.size()];
		iweArray = iweList.toArray(iweArray);

		String[] ediArray = new String[ediList.size()];
		ediArray = ediList.toArray(ediArray);

		for (String s : iweArray) {

			s = s.replaceAll(" ", "-");
			if (s.contains(",,,")) {
				s = s.replaceAll(",,,", "/");
			}
			if (s.contains(",,")) {
				s = s.replaceAll(",,", "/");
			}
			if (s.contains(",")) {
				s = s.replaceAll(",", "/");
			}
			if (s.contains("(")) {
				s = s.replace("(", "");
			}
			if (s.contains(")")) {
				s = s.replace(")", "");
			}
			if (s.contains("&")) {
				s = s.replace("&", "and");
			}
			s = s.replaceAll("^\"|\"$", "");
			for (String m : ediArray) {
				if (s.contains(m)) {
					System.out.println(s.toLowerCase().replaceAll("-+$", ""));
				}
			}
		}

	}
}
