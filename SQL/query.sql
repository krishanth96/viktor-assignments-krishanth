
-- Get the names of the running Projects
SELECT Name
FROM Project
WHERE FinishedAt IS NULL;


-- Get the number of finished Projects per Company
SELECT CompanyId, COUNT(*) AS FinishedProjectsCount
FROM Project
WHERE FinishedAt IS NOT NULL
GROUP BY CompanyId;

-- Get the Company Names that have 2 or more different Projects with the same Name
SELECT c.Name
FROM (
    SELECT e.IdCompany
    FROM Project p
    JOIN Employee e ON p.IdEmployee = e.IdEmployee
    GROUP BY e.IdCompany, p.Name
    HAVING COUNT(*) >= 2
) AS MultiProjectCompanies
JOIN Company c ON c.IdCompany = MultiProjectCompanies.IdCompany;

