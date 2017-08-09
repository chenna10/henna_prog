package adobeTaxonomy;

public class AemTaxonomyTax {
	
	private String aemTax;
	/**
	 * @param panTax
	 * @param aemTax
	 */
	public AemTaxonomyTax(String aemTax) {
		super();
		this.aemTax = aemTax;
	}
	/**
	 * @return the aemTax
	 */
	public String getAemTax() {
		return aemTax;
	}
	/**
	 * @param aemTax the aemTax to set
	 */
	public void setAemTax(String aemTax) {
		this.aemTax = aemTax;
	}
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return aemTax;
	}

}

