# Results

# Taxi Dataset Analysis:
The data obtained from both the Kubernetes cluster and Google Cloud Dataproc Cluster were consistent with eachother

- **Daily Trip Volume**

  Objective: 
  We aimed to measure how the number of taxi trips varied by day during early January 2013 to understand general activity patterns in New York City.

<img width="1200" height="600" alt="trips_per_day" src="https://github.com/user-attachments/assets/75310e3e-90f1-4e32-8ea3-38536ef7fb42" />
  
- Findings: 
  The dataset includes 365 daily records from January through December 2013. Trip counts ranged between roughly 390,000 and 480,000 per day, with consistent activity across the year. Days with higher totals tended to align     with weekends and holidays, reflecting increased leisure transportation.
  


- **Payment Type Distribution**

  Objective: 
  We sought to understand how passengers paid for their rides and the relative frequency of each payment method.

<img width="1000" height="600" alt="payment_mix" src="https://github.com/user-attachments/assets/65868b6d-c4ab-4331-bc11-e96f2cfd993a" />

  Findings: 
  Credit card and cash payments dominated the data, accounting for the vast majority of trips. Credit card transactions slightly outnumbered cash ones, suggesting a growing reliance on electronic payments. A small fraction     of trips used other categories such as corporate or discount accounts.



- **Hourly Trip Distribution**

  Objective: 
  We wanted to examine when taxi trips were most frequent during a typical day to identify demand peaks.

<img width="1000" height="600" alt="busiest_hours" src="https://github.com/user-attachments/assets/f1b3d98c-2767-4f77-a106-fb40ac5305e9" />
  
  Findings:
  Trip volume was highest around midnight and during the morning commute hours from 7 to 9 a.m. This pattern suggests strong activity during nightlife periods and daily work commutes. Lower trip counts were observed in mid-    afternoon and early evening hours.



- **Trip Distance Distribution**

  Objective: 
  We measured how trip frequency changed with distance to understand travel behavior and demand concentration.

<img width="1000" height="600" alt="trip_lengths" src="https://github.com/user-attachments/assets/19634426-c0b3-4ea9-87e2-a900862b2079" />

  Findings:
  Short-distance trips under 3 miles were the most common, representing the majority of all rides. As trip distance increased, the number of trips decreased. Only a small portion of trips exceeded 10 miles, confirming that     most taxi usage occurs within short urban ranges.




- **Google Cloud Dataproc Cluster Specs:**
- Nodes and machine shapes
Master: 1× n4-standard-2 (2 vCPU, ~8 GB RAM), boot disk 60 GB Hyperdisk Balanced
Workers: 4× n4-standard-2 (each 2 vCPU, ~8 GB RAM), boot disk 110 GB Hyperdisk Balanced
Spark properties (key defaults): executor.instances=2, executor.cores=1, executor.memory=2893m, driver.memory=2048m, scheduler=FAIR, DataprocSparkPlugin enabled

- Execution time from Spark History:
   
<img width="1723" height="388" alt="Screenshot 2025-10-30 at 10 14 00 PM" src="https://github.com/user-attachments/assets/7d361b4f-e664-496c-bd2f-29ed8270fcfb" />

Execution time was 15 minutes

- Cost:

<img width="1411" height="203" alt="GC Demo Cost" src="https://github.com/user-attachments/assets/ea33d2c4-faaf-4423-9575-3eb481643274" />




- **Kubernetes Cluster Specs:**
- Nodes and machine shapes
Master: 1× (~8 GB RAM)
Workers: 4× (~8 GB RAM)

- Execution time from Spark History:

<img width="1724" height="462" alt="Screenshot 2025-10-31 at 8 28 56 PM" src="https://github.com/user-attachments/assets/6a3c7d33-1f3c-4fc8-a746-4268c515be38" />

Execution time was 9.4 minutes


## Summary and Analysis

- Data consistency:
  - Outputs from both the Kubernetes and Google Cloud Dataproc clusters are reported as consistent, indicating reproducible analytics across environments.

- Platform performance comparison:
  - Dataproc (n4-standard-2, 1× master + 4× workers; FAIR scheduler; modest driver/executor memory): Completed in ~15 minutes.
  - Kubernetes (1× master + 4× workers, each ~8 GB RAM): Completed faster at ~9.4 minutes.
  - Interpretation: For this workload and configuration, the Kubernetes deployment executed the Spark job ~37% faster. Differences may stem from cluster/runtime tuning, scheduling overheads, storage locality, or image/runtime optimizations. Results show that a well-configured K8s environment can be at least competitive and in this run, faster—than the managed Dataproc setup.

- Takeaways and next steps:
  - Both platforms produced consistent analytical results.
  - For this job, Kubernetes delivered lower wall-clock time than Dataproc given the stated configurations.

Overall, the analysis shows that a Kubernetes-based Spark deployment can perform very well compared to a Dataproc setup for this workload under the tested configurations.

