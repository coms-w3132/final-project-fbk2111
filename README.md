# COMS W3132 Individual Project

## Author
Filimon Keleta, fbk2111

## Project Title
Cryptotrading bot in Kraken (paper trading simulation)

## Project Description

My project aims to develop a comprehensive cryptotrading simulation bot specifically tailored for paper trading, ensuring no real money is involved. The bot will be equipped to execute buy and sell orders, set limiting prices, and implement trading strategies at positions designated by the user-defined strategy. With a focus on automation and accuracy, the program will seamlessly navigate the complexities of cryptocurrency markets, compiling order book data, and providing detailed trade execution records.

At its core, the project addresses the challenge of effectively testing and refining trading strategies in a risk-free environment. By offering functionalities such as order placement, strategy implementation, and performance analysis, the bot empowers traders to experiment with various approaches without financial repercussions. Throughout the semester, my main goals include refining the bot's trading algorithm for optimal decision-making, enhancing user interaction through intuitive controls, and ensuring comprehensive reporting of trading activities.

I anticipate that this project will be of significant interest to cryptocurrency traders seeking to refine their strategies in a safe and controlled environment. By offering a reliable tool for paper trading simulation, complete with automated execution and strategy analysis capabilities, my project aims to streamline the process of strategy development and optimization in the dynamic realm of cryptocurrency trading.
  
## Timeline

*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*

| Date               | Milestone                                                                                              | Deliverables                | Git tag    |
|--------------------|--------------------------------------------------------------------------------------------------------|-----------------------------|------------|
| **March&nbsp;29**  | Submit project description                                                                             | README.md                   | proposal   |
| **April&nbsp;5**   | Update project scope/direction based on instructor/TA feedback                                         | README.md                   | approved   |
| **April&nbsp;12**  | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs | milestone1 |
| **April&nbsp;19**  | Progress on implementation (define your own goals)                                                     | Source code, unit tests     | milestone2 |
| **April&nbsp;26**  | Completely (or partially) finished implementation                                                      | Source code, documentation  | milestone3 |
| **May&nbsp;10**    | Final touches (conclusion, documentation, testing, etc.)                                               | Conclusion (README.md)      | conclusion |

*The column Deliverables lists deliverable suggestions, but you can choose your own, depending on the type of your project.*

## Requirements, Features and User Stories

1. Real-time Market Analysis: Utilize Kraken's API to fetch real-time market data, including price movements, order book depth, and trade history, for accurate analysis.
2. Customizable Trading Strategies: Develop a modular and flexible trading strategy system that allows users to define their own criteria for buying and selling cryptocurrencies. Strategies should be adaptable to different market conditions and adjustable parameters.
3. Automated Execution or Manual Control: Provide options for both automated execution based on predefined strategies and manual control where users can input specific instructions for trading actions.
4. Market Orders and Limit Orders: Implement functionality to execute both market orders and limit orders, enabling users to buy or sell cryptocurrencies at the current market price or at a specified price respectively.
5. Risk Management and Profit Maximization: Integrate risk management techniques to monitor market volatility, minimize losses, and maximize profits. The algorithm should dynamically adjust trading parameters to optimize performance while considering market slippage and transaction fees.
6. Data Query and Historical Analysis: Develop a data query module to store and retrieve historical transaction data and market prices for backtesting and analysis purposes. This module should efficiently manage and organize large datasets for comprehensive market insights.
7. Performance Tracking and Reporting: Provide users with detailed performance metrics and reports, including trade execution logs, profit/loss summaries, and strategy effectiveness analysis. This allows users to evaluate the success of their trading strategies and make informed decisions for future trades.
8. Security and Reliability: Ensure the algorithm's robustness and reliability by implementing secure authentication mechanisms for accessing Kraken's API, handling error responses gracefully, and implementing failover mechanisms to prevent disruptions in trading operations.
9. Scalability and Efficiency: Design the algorithm to be scalable to handle large volumes of data and trading requests efficiently. Employ optimization techniques to minimize latency and ensure real-time responsiveness, crucial for time-sensitive trading decisions.

Requirement Analysis:

- Software: Development will primarily utilize programming languages such as Python for algorithmic trading logic, data analysis, and API integration with Kraken. Additional libraries and frameworks may be used for specific functionalities such as data storage, visualization, and statistical analysis.
- Hardware: The software can run on standard computing hardware, including personal computers or cloud-based servers. It should be capable of handling high-frequency trading tasks efficiently, with sufficient processing power and memory resources.
- API Integration: Utilize Kraken's API for accessing market data, placing orders, and managing trading activities. Ensure seamless integration with the API by following best practices for authentication, error handling, and rate limiting.
- Data Management: Implement a robust data management system for storing and retrieving transaction history, market prices, and other relevant data. Consider using database systems or file storage solutions for efficient data storage and retrieval.
- User Interface: Develop a user-friendly interface for interacting with the trading algorithm, allowing users to configure trading strategies, monitor performance, and access historical data. The interface should be intuitive, responsive, and customizable to meet diverse user needs.
  
Product Analysis:

- Market Potential: With the increasing popularity of cryptocurrency trading, there is a significant demand for advanced trading algorithms that can automate trading strategies and optimize profitability. Our product aims to cater to this market demand by providing a comprehensive solution for cryptocurrency traders.
- Competitive Landscape: There are existing trading bots and platforms in the market offering similar functionalities. However, our product distinguishes itself by focusing on advanced trading algorithms tailored for Kraken's platform, offering customizable strategies, real-time market analysis, and robust risk management features.
- Target Audience: Our target audience includes cryptocurrency traders ranging from individual investors to institutional traders looking for sophisticated trading tools to enhance their trading strategies and maximize returns. Additionally, our product appeals to cryptocurrency enthusiasts and developers interested in algorithmic trading and market analysis.

 User Story:
 
As a cryptocurrency trader, I want to utilize an advanced trading algorithm that can automate my trading strategies and optimize profitability in real-time. I want the algorithm to provide customizable trading strategies based on market analysis and historical data, allowing me to adapt to changing market conditions and maximize returns. I want the algorithm to seamlessly integrate with Kraken's API, enabling fast and reliable execution of market orders and limit orders. I also want access to comprehensive performance metrics and reports, allowing me to evaluate the success of my trading strategies and make informed decisions for future trades. Furthermore, I want the algorithm to prioritize security and reliability, ensuring the safety of my funds and providing robust risk management features to minimize losses. Overall, I expect the algorithm to enhance my trading experience by providing advanced trading functionalities, real-time market insights, and efficient execution capabilities.

## Technical Specification
*Detail the main algorithms, libraries, and technologies you plan to use. Explain your choice of technology and how it supports your project goals.*
I will be using:
  Pandas: Pandas is chosen for its versatility and efficiency in handling structured data, essential for processing market data and trade history in real-time. Its rich set of functions and operations enable us to perform complex data transformations and analysis, supporting the development of advanced trading strategies and risk management techniques.
  Asyncio (async/await): Asyncio is selected to enable asynchronous programming in our trading algorithm, enhancing performance and responsiveness by allowing concurrent execution of tasks. This technology choice aligns with our project goal of developing a high-performance trading bot capable of processing real-time market data and executing trades promptly, thereby maximizing trading opportunities and minimizing latency.
  Time Library: The time library provides essential functionalities for time management and scheduling in our trading algorithm. By accurately measuring time intervals, scheduling trading actions,       and implementing timeout mechanisms, we ensure timely execution of trading strategies and efficient utilization of market opportunities, supporting our project goal of optimizing profitability      and  minimizing risks.
  API Management Library (e.g., requests): An API management library like requests is indispensable for interacting with Kraken's API and accessing cryptocurrency market data. Its simplicity and       robustness make it an ideal choice for handling HTTP requests, managing authentication, and processing API responses efficiently. By leveraging this technology, we ensure seamless integration       with   Kraken's platform, enabling reliable execution of trading actions and accurate analysis of market dynamics.
  TA-Lib: A library for technical analysis, providing functions for calculating various technical indicators commonly used in trading strategies.
  NumPy: A fundamental package for scientific computing with Python, useful for numerical operations and array manipulation required for algorithmic trading.
  Backtrader: A popular Python library for backtesting trading strategies, allowing you to simulate trades using historical data, evaluate performance metrics, and optimize strategies.
  PyAlgoTrade: Another backtesting library that supports event-driven and vectorized backtesting, providing tools for strategy development and performance analysis.
  PyQt or PySide: Python bindings for the Qt framework, suitable for creating desktop GUI applications with rich graphical interfaces.
  Dash or Flask: Web frameworks for building interactive web applications in Python, allowing you to create web-based UIs for monitoring and managing trading activities.
  Keyring: A library for securely storing and accessing sensitive data like API keys and passwords, integrating with system-specific keyring services for enhanced security.
  Optuna: A hyperparameter optimization framework that can be used to automatically optimize the parameters of your trading strategies based on performance metrics and backtesting results.

## System or Software Architecture Diagram
   >>means call
  Trading Bot >> Api call >> fetching market prices (market data) >> Trading strategy >> calls queried data >> Trading Strategy >> Trading Bot (execution happens here) >> Data queried.

## Development Methodology
For organizing and progressing the development of the project, I plan to adopt an agile software development methodology with elements of the Scrum framework. Here's a breakdown of how I'll organize and progress the work:
Development Plan:
1. GitHub Projects Board:
   - I will utilize the GitHub Projects board to track progress on tasks and milestones. This will help me organize tasks into different columns (e.g., To-Do, In Progress, Done) and prioritize them based on importance and urgency.
2. GitHub Issues:
   - GitHub Issues will be used to keep track of issues, bugs, and feature requests. Each issue will be appropriately labeled, assigned, and categorized for easy management and resolution.
3. Git Branches and Pull Requests:
   - I will use separate Git branches for development, feature implementation, and bug fixes. Each feature or task will have its own branch, and I'll create pull requests to merge changes into the main branch after code review and testing.
4. GitHub Actions:
   - GitHub Actions will be set up for automated testing and deployment pipelines. This will include running unit tests, integration tests, and code linting checks on every pull request to ensure code quality and reliability.
5. GitHub Wiki:
   - The GitHub Wiki will serve as documentation and notes for the project. I'll use it to document project requirements, architecture, setup instructions, usage guidelines, and any other relevant information for contributors and users.
Testing and Evaluation:
- Manual and Automated Testing:
   - I plan to conduct both manual and automated testing to ensure the functionality and reliability of the project. Manual testing will involve hands-on testing of features and functionalities by simulating user interactions and scenarios. Automated testing will include unit tests and integration tests to verify individual components and their interactions.
- Testing Frameworks and Libraries:
   - For automated testing, I'll use popular testing frameworks and libraries such as pytest for writing and running unit tests, hypothesis for property-based testing, and Selenium for end-to-end testing of user interfaces. These frameworks will help ensure code correctness, identify bugs, and prevent regressions during development.
- Continuous Integration (CI):
   - Continuous integration will be implemented using GitHub Actions to automatically run tests on every code change. This will ensure that new features and bug fixes are thoroughly tested and integrated into the codebase without introducing breaking changes.
By following this development methodology, I aim to maintain a structured and efficient development process, track progress effectively, collaborate with contributors seamlessly, and deliver a high-quality and reliable cryptocurrency trading algorithm.

## Potential Challenges and Roadblocks
API Limitations and Rate Limits:
  Challenge: Kraken's API may have rate limits or restrictions on the number of requests per minute/hour, which could affect the responsiveness and performance of the trading algorithm.
  Solution: Implement rate limiting mechanisms in the trading algorithm to adhere to Kraken's API usage policies. Use techniques like request throttling, backoff strategies, and caching to manage      API calls efficiently. Consult Kraken's documentation and seek guidance from the instructor or TAs if needed.
Market Data Quality and Reliability:
  Challenge: Market data obtained from Kraken's API may be incomplete, delayed, or inconsistent, leading to inaccurate analysis and decision-making.
  Solution: Implement data validation and error handling mechanisms to detect and handle anomalies in market data. Consider using multiple data sources or historical data backups for validation and   comparison. Collaborate with the instructor or TAs to troubleshoot data-related issues and explore alternative data providers if necessary.
Complexity of Trading Strategies:
  Challenge: Designing and implementing advanced trading strategies with complex logic and parameters can be challenging, requiring in-depth understanding of financial markets and algorithmic trading principles.
  Solution: Break down trading strategies into smaller, manageable components and implement them incrementally. Conduct thorough research on trading strategies, leverage existing libraries and        frameworks, and seek guidance from financial experts or instructors to validate and refine strategies effectively.
Concurrency and Asynchronous Programming:
  Challenge: Implementing asynchronous programming for handling multiple concurrent tasks, such as fetching market data, analyzing strategies, and executing trades, can be complex and error-prone.
  Solution: Utilize asynchronous programming libraries like asyncio and async/await to manage concurrent tasks efficiently. Follow best practices for error handling, resource management, and task coordination. Seek assistance from instructors or TAs for understanding asynchronous programming concepts and troubleshooting concurrency issues.

## Additional Resources
None as of now, but CCXT implementation might be helpful

## Conclusion and Future Work
The project is a big line, helps use computer science in the releam of finance and financial engineering. Future direction: might be using ML or LLM to train the trading strategy to make accurate and fast implementation that can maximize profit. Data quering in a virtual machine likely possible using AWS or Azure. efficient server based API implementation to decrease latency and minimize market slippage.

