# Technical Interview Exercise — Lambda to Kappa Migration

## Context

Our company runs an **e-commerce platform**.

The current data platform is based on **Lambda Architecture**:

- **Batch pipeline**
  - Nightly processing with **Spark**
  - Data stored in **S3**
- **Streaming pipeline**
  - Real-time processing with **Flink**
  - Events ingested via **Kafka**
- A **real-time dashboard** consumes streaming results
- Historical aggregations come from the batch layer

Maintaining **two separate codebases** (Spark + Flink) that implement similar business logic has become very costly and error-prone.

The **CTO wants to migrate to Kappa Architecture**.

---

## Current Architecture (As-Is)

### Diagram

```mermaid
flowchart LR
    U[Users / E‑commerce Events] --> K[Kafka]

    %% Speed Layer
    K --> F[Flink<br/>Streaming Pipeline]
    F --> RT[Real-Time Dashboard]

    %% Batch Layer
    K --> S3[(S3 Data Lake)]
    S3 --> SP[Spark<br/>Nightly Batch Job]
    SP --> BV[Batch Views]

    %% Serving
    RT --> D[Analytics / Reporting]
    BV --> D