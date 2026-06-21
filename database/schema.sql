-- Create the vehicles table
CREATE TABLE vehicles (
    vehicle_id  INT PRIMARY KEY,
    make        VARCHAR(50),
    model       VARCHAR(50),
    year        INT
);

-- Create the claims table
CREATE TABLE claims (
    claim_id     INT PRIMARY KEY,
    vehicle_id   INT,
    repair_cost  DECIMAL(10, 2),
    claim_status VARCHAR(20),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);
