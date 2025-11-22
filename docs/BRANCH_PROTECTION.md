# Branch Protection Guidelines

This document outlines the recommended branch protection settings for the `main` branch to maintain code quality, stability, and collaboration standards.

---

## Table of Contents

- [Why Branch Protection?](#why-branch-protection)
- [Recommended Settings for `main` Branch](#recommended-settings-for-main-branch)
- [Enabling Branch Protection (UI Steps)](#enabling-branch-protection-ui-steps)
- [Enabling Branch Protection (REST API)](#enabling-branch-protection-rest-api)
- [Automation with GitHub Actions](#automation-with-github-actions)
- [Exception Process](#exception-process)
- [Troubleshooting](#troubleshooting)

---

## Why Branch Protection?

Branch protection ensures:
- **Code Quality**: All changes are reviewed before merging
- **Stability**: Tests and checks must pass before deployment
- **Collaboration**: Clear process for contributions
- **Security**: Prevents accidental or malicious direct commits
- **History**: Maintains a clean, traceable commit history

---

## Recommended Settings for `main` Branch

Apply the following protection rules to the `main` branch:

### ✅ Required Settings

1. **Require a pull request before merging**
   - ✅ Require approvals: **1**
   - ✅ Dismiss stale pull request approvals when new commits are pushed
   - ⬜ Require review from Code Owners (optional, if CODEOWNERS file exists)

2. **Require status checks to pass before merging**
   - ✅ Require branches to be up to date before merging
   - Add required status checks once CI/CD is configured (e.g., "build", "test", "lint")

3. **Require conversation resolution before merging**
   - ✅ All PR comments must be resolved before merge

4. **Require signed commits** (optional but recommended)
   - ⬜ Enable if your organization requires commit signature verification

5. **Require linear history** (optional)
   - ⬜ Enable to enforce squash merging or rebasing (prevents merge commits)

6. **Do not allow bypassing the above settings**
   - ✅ Enable to enforce rules for everyone (including admins)
   - ⬜ Allow specific users/teams to bypass (for emergency hotfixes)

7. **Restrict who can push to matching branches**
   - ✅ Enable and restrict to specific users or teams (maintainers only)
   - Or leave unchecked if all pushes must go through PRs

8. **Allow force pushes**
   - ❌ Disable (force pushes can rewrite history)

9. **Allow deletions**
   - ❌ Disable (prevents accidental branch deletion)

---

## Enabling Branch Protection (UI Steps)

### Step 1: Navigate to Repository Settings
1. Go to your repository on GitHub
2. Click **Settings** (top navigation bar)
3. In the left sidebar, click **Branches**

### Step 2: Add Branch Protection Rule
1. Under "Branch protection rules", click **Add rule**
2. In "Branch name pattern", enter: `main`

### Step 3: Configure Protection Settings
Apply the recommended settings listed above:

#### Protect matching branches
- ✅ **Require a pull request before merging**
  - Set "Require approvals" to **1**
  - ✅ Check "Dismiss stale pull request approvals when new commits are pushed"

- ✅ **Require status checks to pass before merging**
  - ✅ Check "Require branches to be up to date before merging"
  - Search and add status checks (e.g., "build", "test") once CI is configured

- ✅ **Require conversation resolution before merging**

- ❌ **Require signed commits** (optional)

- ❌ **Require linear history** (optional)

- ✅ **Do not allow bypassing the above settings** (for admin enforcement)

#### Rules applied to everyone including administrators
- ⬜ **Allow force pushes** → Keep unchecked (disabled)
- ⬜ **Allow deletions** → Keep unchecked (disabled)

### Step 4: Save Changes
1. Scroll to the bottom of the page
2. Click **Create** or **Save changes**

---

## Enabling Branch Protection (REST API)

For automation or programmatic setup, use the GitHub REST API:

### API Endpoint
```
PUT /repos/{owner}/{repo}/branches/{branch}/protection
```

### Example Request

```bash
curl -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/nexageapps/LLM/branches/main/protection \
  -d '{
    "required_status_checks": {
      "strict": true,
      "contexts": []
    },
    "enforce_admins": true,
    "required_pull_request_reviews": {
      "dismissal_restrictions": {},
      "dismiss_stale_reviews": true,
      "require_code_owner_reviews": false,
      "required_approving_review_count": 1,
      "require_last_push_approval": false
    },
    "restrictions": null,
    "required_conversation_resolution": true,
    "allow_force_pushes": false,
    "allow_deletions": false
  }'
```

### Notes
- Replace `YOUR_GITHUB_TOKEN` with a personal access token (classic) with `repo` scope or a fine-grained token with repository administration permissions
- Add status check contexts (e.g., `["build", "test"]`) once CI workflows are running
- For organization-wide automation, consider using a GitHub App instead of PATs

---

## Automation with GitHub Actions

### Option 1: Apply Branch Protection via Workflow

Create a workflow (`.github/workflows/apply-branch-protection.yml`) to automatically enforce protection settings:

```yaml
name: Apply Branch Protection

on:
  workflow_dispatch:  # Manual trigger
  schedule:
    - cron: '0 0 * * 0'  # Weekly check (Sundays at midnight UTC)

permissions:
  contents: read
  # Note: This workflow requires admin-level token or GitHub App

jobs:
  apply-protection:
    runs-on: ubuntu-latest
    steps:
      - name: Apply Branch Protection
        run: |
          curl -X PUT \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer ${{ secrets.ADMIN_GITHUB_TOKEN }}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/repos/${{ github.repository }}/branches/main/protection \
            -d '{
              "required_status_checks": {"strict": true, "contexts": []},
              "enforce_admins": true,
              "required_pull_request_reviews": {
                "dismiss_stale_reviews": true,
                "required_approving_review_count": 1
              },
              "required_conversation_resolution": true,
              "allow_force_pushes": false,
              "allow_deletions": false
            }'
```

**⚠️ Important:** This requires storing an admin-level GitHub token as a repository secret. Consider security tradeoffs:
- **Pros**: Automated enforcement, easy to maintain
- **Cons**: Storing admin PATs in secrets is a security risk
- **Alternative**: Use a GitHub App with limited permissions

### Option 2: Manual Enforcement
Maintainers should manually verify branch protection settings quarterly or after major repository changes.

---

## Exception Process

In rare cases, exceptions to branch protection may be necessary (e.g., critical hotfixes, security patches).

### Requesting an Exception

1. **Open an Issue**: Create a GitHub issue explaining:
   - Why the exception is needed
   - What changes will be made
   - Urgency and impact assessment

2. **Tag a Maintainer**: Mention repository maintainers for review

3. **Security Issues**: For security vulnerabilities, follow the security disclosure process in [CONTRIBUTING.md](../CONTRIBUTING.md)

### Granting an Exception

Maintainers with admin access can:
1. Temporarily disable specific protection rules
2. Make the necessary changes
3. Re-enable protection rules immediately after

**⚠️ Warning:** Document all exceptions in an issue for audit trail purposes.

---

## Troubleshooting

### Issue: "Required status checks are not passing"
- **Cause**: CI workflows haven't run yet or failed
- **Solution**: 
  - Wait for CI to complete
  - Fix any failing tests
  - If CI is not configured yet, remove required status checks temporarily

### Issue: "Cannot merge without approval"
- **Cause**: No approving reviews on the PR
- **Solution**: Request review from a maintainer

### Issue: "Branch is out of date with base branch"
- **Cause**: New commits on `main` since the PR was opened
- **Solution**: 
  ```bash
  git checkout your-branch
  git pull origin main
  git push
  ```

### Issue: "Admin cannot bypass protection rules"
- **Cause**: "Do not allow bypassing" is enabled
- **Solution**: 
  - This is intentional for security
  - For emergencies, temporarily disable the rule, make changes, re-enable

### Issue: "Cannot enable protection - insufficient permissions"
- **Cause**: You need admin access to the repository
- **Solution**: Contact the repository owner to grant admin permissions or request they enable protection

---

## Additional Resources

- [GitHub Docs: About Protected Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub REST API: Branch Protection](https://docs.github.com/en/rest/branches/branch-protection)
- [Best Practices for Branch Protection](https://github.blog/2021-01-21-branch-protection-rules/)

---

## Questions or Suggestions?

If you have questions about branch protection or suggestions for improving these guidelines, please:
- Open a [Discussion](https://github.com/nexageapps/LLM/discussions) (if enabled)
- Open an issue with the `documentation` label
- Contact the maintainer

**Last Updated**: November 2025
