# Re-Active AI Agent with Large Number of Tools
## Example of using langgraph nodes and edges with langchain tools 

### Load, Split, Emnbed, Store 
- Entrypoint is to have a document vectorized in this example I used local Qdrant and 2021 report https://bitcoingroup.com/images/PDF/FB_2021/BitcoinGroup_GB2021_EN.pdf

### Agent execution
- The multi tools agent selects the correct tool including RAG to provide better analisys of the report.
- Requires OpenAI API Key and local Vector DB with above report loaded

``` 
# main.py
from report_agent import app

query = {'messages': [('user', 'what is the BitcoinGroup report about')]}

events=app.stream(query,{}, stream_mode="values") # for now we don't pass any config
for ev in events:
    print(ev["messages"][-1].pretty_print())
```
- The RAG Results would look something like this

 ================================== Ai Message ==================================

The BitcoinGroup report provides detailed information about Bitcoin Group SE, a capital investment company and consulting firm focused on Bitcoin and blockchain business models. Here is an analysis based on the provided information:

1. Core Business Model:
   - Bitcoin Group SE is a capital investment company and consulting firm with a focus on Bitcoin and blockchain business models.
   - The company generates revenue from consulting and brokerage services for cryptocurrency and blockchain business models.
   - Bitcoin Group SE holds a 100% stake in futurum bank AG, located in Frankfurt am Main.

2. Revenue Drivers:
   - Revenue streams include consulting and brokerage services for cryptocurrency and blockchain business models.
   - The company's revenue was EUR 25.4 million in the reporting year, showing significant growth from the previous year.
   - Market conditions, such as the sharp increase in the price and high volatility of Bitcoin, have positively impacted revenue.

3. Strategic Position:
   - Competitive advantages include expertise in Bitcoin and blockchain technologies.
   - The company has a 100% stake in futurum bank AG and plans further participations in the cryptocurrency field.
   - Growth initiatives include expanding partnerships and target markets to enhance profitability.

4. Market Context & Risks:
   - Regulatory environment plays a significant role in the market, with attention to government regulations on cryptocurrencies.
   - Major risk factors include cybersecurity threats, loss of cryptocurrencies, and regulatory uncertainties.
   - The company is exposed to market trends and performance indicators specific to the cryptocurrency industry.

5. Financial Metrics:
   - Trading volumes and revenue figures contribute to the company's financial performance.
   - The company reported a net profit after taxes of EUR 13,373,717 in the reporting year.
   - Growth rates and market share data are key financial metrics monitored by the company.

Overall, the BitcoinGroup report highlights the company's strategic focus on cryptocurrency and blockchain technologies, revenue drivers, competitive positioning, market context, and financial performance metrics.
 
