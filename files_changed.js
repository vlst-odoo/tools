const { execSync } = require('child_process');

// const branch = "odoo";
const branch = "enterprise";
const gitDiffCommand = `cd /home/odoo/src/${branch} && git diff --name-only HEAD HEAD~1`;
const gitDiffOutput = execSync(gitDiffCommand, { encoding: 'utf8' });

const addonList = Array.from(new Set(gitDiffOutput.split('\n').map(line => {
    const startIndex = branch === 'odoo' ? line.indexOf('/') + 1 : 0;
    const endIndex = line.indexOf('/', startIndex);
    return line.substring(startIndex, endIndex !== -1 ? endIndex : undefined);
  })));
const noOfModulesPerLine = 5;
  const output = addonList.reduce((result, addon, index) => {
  const line = index % noOfModulesPerLine === 0 && index != 0 ? ',\n' : '';
  const separator = index === 0 ? '' : ',';
  return result + line + (line ? addon : separator + addon);
}, '');

  console.log(output);