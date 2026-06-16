-- Audit volume by department

SELECT department,
COUNT(*)
FROM audit_findings
GROUP BY department;


-- Severity distribution

SELECT severity,
COUNT(*)
FROM audit_findings
GROUP BY severity;


-- Top suppliers by defect rate

SELECT suppliername,
AVG(defectrate)
FROM supplier_quality
GROUP BY suppliername
ORDER BY AVG(defectrate) DESC
LIMIT 10;


-- Best supplier region

SELECT supplierregion,
AVG(defectrate)
FROM supplier_quality
GROUP BY supplierregion
ORDER BY AVG(defectrate);


-- Units received trend

SELECT month,
SUM(unitsreceived)
FROM supplier_quality
GROUP BY month;