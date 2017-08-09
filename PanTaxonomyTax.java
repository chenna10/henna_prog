package adobeTaxonomy;

public class PanTaxonomyTax {
	
	private String panTax;

	/**
	 * @param panTax
	 */
	public PanTaxonomyTax(String panTax) {
		super();
		this.panTax = panTax;
	}

	/**
	 * @return the panTax
	 */
	public String getPanTax() {
		return panTax;
	}

	/**
	 * @param panTax the panTax to set
	 */
	public void setPanTax(String panTax) {
		this.panTax = panTax;
	}

	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return panTax;
	}

}

