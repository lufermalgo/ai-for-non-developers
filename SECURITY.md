# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly by emailing [fmaldonado@summan.com](mailto:fmaldonado@summan.com) with the subject line "Security Vulnerability Report."

**Please do not open a public issue for security vulnerabilities.**

Include in your report:
- A description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact
- Suggested fix (if you have one)

We will:
1. Acknowledge receipt within 48 hours
2. Investigate the issue
3. Work with you to develop a fix
4. Coordinate a responsible disclosure timeline

## Security Considerations

This framework is designed to work with AI tools that have autonomous file manipulation and terminal execution capabilities. Users should:
- Only use this framework with tools and tokens they trust
- Review generated code before executing it
- Be cautious with sensitive data in prompts
- Use `.gitignore` and `.aind/` to keep project context private

## Dependencies

We regularly review and update dependencies for known vulnerabilities. If you find a vulnerable dependency, please report it following the process above.
