package adobeTaxonomy;

public class PanTaxonomyID {
	
private String panID;
	
	

	/**
	 * @param panID
	 */
	public PanTaxonomyID(String panID) {
		super();
		this.panID = panID;
	}

	/**
	 * @return the panID
	 */
	public String getPanID() {
		return panID;
	}

	/**
	 * @param panID the panID to set
	 */
	public void setPanID(String panID) {
		this.panID = panID;
	}


	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return panID + ",";
	}
	


}

