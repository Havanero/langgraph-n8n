# Re-Active AI Agent with Large Number of Tools
## Example of using langgraph nodes and edges with langchain tools 

### Load, Split, Emnbed, Store 
- Entrypoint is to have a document vectorized in this example I used local Qdrant and 2021 report https://bitcoingroup.com/images/PDF/FB_2021/BitcoinGroup_GB2021_EN.pdf

### Agent execution
- The multi tools agent selects the correct tool including RAG to provide better analisys of the report.
- Requires OpenAI API Key and local Vector DB with above report loaded

``` 
# installation 
pip install -e .
from report_agent import app
gen-ai run 'what is the BitcoinGroup report about'

```
- The RAG Results would look something like this

================================== Ai Message ==================================

The Bitcoin report of 2021 provides a comprehensive analysis of Bitcoin Group SE's financial performance and strategic positioning during the fiscal year. Here's a structured overview based on the report:

1. **Core Business Model**
   - **Primary Business**: Bitcoin Group SE is a capital investment company and consulting firm focused on Bitcoin and blockchain business models.
   - **Key Subsidiaries**: The company holds a 100% stake in futurum bank AG, which operates the cryptocurrency trading platform Bitcoin.de.
   - **Revenue-Generating Activities**: Revenue is primarily generated from consulting and brokerage services for cryptocurrencies.
   - **Locations**: The company is headquartered in Herford, Germany.

2. **Revenue Drivers**
   - **Revenue Streams**: The main revenue stream is brokerage fees from the Bitcoin.de marketplace.
   - **Quantitative Metrics**: Revenue increased to EUR 25.4 million in 2021 from EUR 15.0 million in 2020, marking a 69.3% rise.
   - **Market Conditions**: The rising popularity of cryptocurrencies and increased trading volumes positively impacted revenue.

3. **Strategic Position**
   - **Competitive Advantages**: The company benefits from its established trading platform and strategic partnerships.
   - **Key Partnerships**: Bitcoin Group SE has a 50% interest in Sineus Financial Services GmbH.
   - **Growth Initiatives**: The company plans to expand its services and increase its stake in cryptocurrency-related companies.
   - **Strategic Goals**: Aims to boost company value and profitability through strategic investments.

4. **Market Context & Risks**
   - **Market Trends**: The cryptocurrency market saw significant growth, with Bitcoin's price appreciating by 74.6% over the year.
   - **Regulatory Environment**: The company operates in a complex regulatory landscape, with potential impacts from government regulations on cryptocurrencies.
   - **Risk Factors**: Major risks include market volatility and regulatory changes.

5. **Financial Metrics**
   - **Trading Volumes**: Increased trading volumes on the Bitcoin.de platform.
   - **Revenue Figures**: Revenue of EUR 25.4 million in 2021.
   - **Growth Rates**: Revenue growth of 69.3% compared to the previous year.
   - **Market Share Data**: The company maintained a strong position in the cryptocurrency trading market.

Overall, the report highlights Bitcoin Group SE's successful fiscal year in 2021, driven by increased demand for cryptocurrencies and strategic business operations.
 
