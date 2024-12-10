
SELECT
    t.teamno,
    t.name AS team_name,
    COALESCE(SUM(s.qty * s.price), 0) AS sales_amount
FROM
    team t
LEFT JOIN
    sales s ON t.teamno = s.teamno
LEFT JOIN
    emp e ON e.empno = s.empno
GROUP BY
    t.teamno, t.name
ORDER BY
    sales_amount DESC;
