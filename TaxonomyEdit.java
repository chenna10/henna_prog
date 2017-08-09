package adobeTaxonomy;

import java.io.BufferedReader; 
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TaxonomyEdit {

	private static final String COMM_DELIMITER = ",";

	public static void readCSVFile(String fileName1, String fileName2, String fileName3) {

		try {
			BufferedReader taxFile = new BufferedReader(new FileReader(fileName1));
			BufferedReader panTaxFile = new BufferedReader(new FileReader(fileName2));
			BufferedReader panIDFile = new BufferedReader(new FileReader(fileName3));
			String aemLine = " ";
			String panTaxLine = " ";
			String panIDLine = " ";
			List<PanTaxonomyID> panId = new ArrayList<PanTaxonomyID>();
			List<PanTaxonomyTax> panTax = new ArrayList<PanTaxonomyTax>();
			List<AemTaxonomyTax> aemTax = new ArrayList<AemTaxonomyTax>();

			taxFile.readLine();
			panTaxFile.readLine();
			panIDFile.readLine();

			int i = 0;
			int j = 0;

			while ((aemLine = taxFile.readLine()) != null) {
				String[] tokens1 = aemLine.split("\n");
				if (tokens1.length > 0) {
					if (tokens1[i].contains("Codifyd-Recommended Taxonomy")) {
						tokens1[i] = tokens1[i].replace("Codifyd-Recommended Taxonomy>",
								"/content/panduit/en/products/");
					}
					if (tokens1[i].contains(">")) {
						tokens1[i] = tokens1[i].replace(">", "/");
					}
					if (tokens1[i].contains(" & ")) {
						tokens1[i] = tokens1[i].replace(" & ", " ");
					}
					if (tokens1[i].contains(", ")) {
						tokens1[i] = tokens1[i].replace(", ", "-");
					}
					if (tokens1[i].contains(" ")) {
						tokens1[i] = tokens1[i].replace(" ", "-");
					}
					AemTaxonomyTax aTax = new AemTaxonomyTax(tokens1[i]);
					System.out.print(aTax.toString().toLowerCase() + " ");
				}
				while ((panTaxLine = panTaxFile.readLine()) != null && (panIDLine = panIDFile.readLine()) != null) {
					if (!aemLine.equals(panTaxLine)) {
						System.out.println();
						aemLine = taxFile.readLine();
						String[] tokens4 = aemLine.split("\n");
						if (tokens4[i].contains("Codifyd-Recommended Taxonomy")) {
							tokens4[i] = tokens4[i].replace("Codifyd-Recommended Taxonomy>",
									"/content/panduit/en/products/");
						}
						if (tokens4[i].contains(">")) {
							tokens4[i] = tokens4[i].replace(">", "/");
						}
						if (tokens4[i].contains(" & ")) {
							tokens4[i] = tokens4[i].replace(" & ", " ");
						}
						if (tokens4[i].contains(", ")) {
							tokens4[i] = tokens4[i].replace(", ", "-");
						}
						if (tokens4[i].contains(" ")) {
							tokens4[i] = tokens4[i].replace(" ", "-");
						}
						System.out.print(tokens4[i].toString().toLowerCase() + " ");
					}
					String[] tokens2 = panTaxLine.split(COMM_DELIMITER);
					String[] tokens3 = panIDLine.split(COMM_DELIMITER);

					if (tokens2.length > 0 && tokens3.length > 0) {

						PanTaxonomyID id = new PanTaxonomyID(tokens3[j]);
						PanTaxonomyTax pTax = new PanTaxonomyTax(tokens2[j]);
						if (aemTax.toString().equals(panTax.toString())) {

							System.out.print(id.toString());

						}

					}

				}

			}
			taxFile.close();
			panTaxFile.close();
			panIDFile.close();

		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String fileName1 = "Taxonomy.csv";
		String fileName2 = "Panduit Tax 5_18_2017.csv";
		String fileName3 = "PanID 5_22_2017.csv";
		readCSVFile(fileName1, fileName2, fileName3);

		input.close();
	}

}
