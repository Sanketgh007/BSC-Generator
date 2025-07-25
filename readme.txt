BSC Generator - Known Bugs and Issues
=====================================

SECURITY ISSUES:
1. Admin Password Verification - Admin password transmitted in plain text via POST in delete_bsc_data function
2. Missing Rate Limiting - No rate limiting on password reset attempts

DATA INTEGRITY ISSUES:
3. Batch ID Generation - Complex batch ID generation could fail with concurrent uploads
4. Date Parsing Vulnerabilities - Multiple date format attempts without proper error handling
5. Missing Organization Validation - Potential cross-organization data access if filtering fails

UI/UX ISSUES:
6. Static File Dependencies - Templates reference static files that may not exist:
   - {% static 'assets/abstract.jpg' %}
   - {% static 'css/tailwind.build.css' %}
7. Error Message Inconsistency - Mixed use of messages.error() and JSON errors

PERFORMANCE ISSUES:
8. Inefficient Database Queries - Multiple separate queries instead of using unions
9. Large File Upload Handling - No file size limits for CSV/Excel uploads

MINOR ISSUES:
10. Hardcoded Values - Password length minimum hardcoded to 6 characters
11. Missing Validation - No validation for numeric fields in target/actual values

NOTES:
- Password reset functionality is implemented and working
- All URL patterns are properly configured
- Application is fully functional with all core features working