-- Insert master asset list into vehicles table
INSERT INTO vehicles VALUES
(1, 'Toyota', 'Camry',   2020),
(2, 'Ford',   'F-150',   2019),
(3, 'Honda',  'Accord',  2021),
(4, 'Chevy',  'Malibu',  2018);

-- Insert transactional history into claims table
INSERT INTO claims VALUES
(101, 1, 1200.00, 'Approved'),
(102, 2,  850.00, 'Pending'),
(103, 3, 3400.00, 'Approved'),
(104, 4,  500.00, 'Denied'),
(105, 1, 2100.00, 'Pending'),
(106, 3,  975.00, 'Denied'),
(107, 2, 4800.00, 'Approved');
