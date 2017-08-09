package scAnalytics;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class parseGoogleAnalytics {
	
	public static String driverPath = "C:/Users/che/Desktop/chromedriver";
	public static WebDriver driver;
	public static String [] productList = []
	
	public static void main (String [] args) {
		
		System.out.println("launching chrome browser");
		System.setProperty("webdriver.chrome.driver", driverPath+"chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().window().maximize();
		String baseUrl = "https://analytics.google.com/analytics/web/#report/content-drilldown/a40992416w70570837p72770040/%3Fexplorer-table.plotKeys%3D%5B%5D%26explorer-table.rowStart%3D0%26explorer-table.rowCount%3D1000%26_r.drilldown%3Danalytics.pagePathLevel1%3A%2Fen%2F%2Canalytics.pagePathLevel2%3A%2Fproduct%2F/";
		
		driver.get(baseUrl);
		
	}
	
	
	
	

}
