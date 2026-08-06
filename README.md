<center>

![](https://raw.githubusercontent.com/ohbm/eCOBIDAS/master/images/ARTEMIS_logo.jpg)

</center>

## Agreed Reporting Template for EEG Methodology - International Standard: template for event-related potentials (ERP)

The goal of the ARTEM-IS is to use insights derived from systematic reviews and guidelines for good checklist design to create dynamic and user-friendly web applications which support EEG researchers in creating detailed human- and machine-readable methods summaries. Currently, ARTEM-IS has launched the first of its tools, ARTEM-IS for ERP, which supports describing a simple ERP experiment, including most of its core methodological aspects (study description, experimental design, hardware, data acquisition, pre-processing, measurement, visualisation, additional comments – artemis.incf.org). ARTEM-IS tools for more complex ERP experiments as well as for other subfields of EEG may follow.

## How to use it

1. The web-app is available **[HERE](https://artemis.incf.org/)**.
2. On the initial page, you can create your account and log in, as well as view a visualization of the basic structure of the information provided in the template.
3. Once logged in, by clicking `Create` in the top right corner, you can create a new, blank template.
4. You can navigate a template by using the menu on top and answer the questions corresponding to the study you are reporting on. This is meant to ensure that you have not forgotten any of the essential information during data collection or later in the methods and results parts of your article.
5. Click `Save` in the top right corner to save any changes.
6. You can view your own saved templates using `My templates` option. For each template, you have the options to make them publicly (in)visible to others, download a human-readable PDF output and download a machine-readable JSON output. All templates are set to private in the beginning.
7. You can view and download publicly available templates by other members using `Browse` menu.
8. You can upload a previously downloaded (in JSON format) templates to your account using `Upload` menu.

You can find output examples on the [OSF page of this project](https://osf.io/ahp3t/).

## Why this project?

It is well known that choices made during recording, preprocessing and analysis of EEG data can affect study outcomes, making it critical to describe EEG methods and the decision-making process thoroughly and transparently. Transparent methods records would allow not only better reproducibility and replicability of EEG research or a better appraisal of the quality of existing studies, but also provide a better basis for novel research, for example by providing meta-scientists with relevant information on published studies. Researchers new to the field of EEG may especially benefit from transparent and thorough reports of EEG studies, as some of them are not beneficiaries of the decades of knowledge contained in unpublished materials like ‘lab handbooks’ which may be passed down in labs with longer traditions.

Despite this, systematic reviews of reporting practices in the field have shown that journal articles do not meet this goal and that guidelines for writing them better have not resulted in a sufficient improvement to reporting transparency. ARTEM-IS is designed to help with this issue as ARTEM-IS reports contain a level of reporting precision higher than what is typically found in journal articles, which can be used as supplements to a publication, as a memory aid when writing a paper, or as records that allow easier metadata extraction in comparison to verbal descriptions in papers.

### Want to know more ?

Read more about the rationale for this project and the design principles we go by in our **[paper](https://www.sciencedirect.com/science/article/pii/S1053811921009939?via%3Dihub)**, and if you agree support us by signing the **[ARTEM-IS statement](https://osf.io/mf97q/)**.

1. Have a look at our **[project on OSF](https://osf.io/pvrn6/)**.
2. **Talks and slides** are available [HERE](https://osf.io/ncav8/).
3. See [CONTRIBUTING.md](src/CONTRIBUTING.md) for information on how to contribute.


## Getting Started

### Browsing / Using the Tool

1. Visit the web app at [artemis.incf.org](https://artemis.incf.org).  
2. Log in or register a new account.  
3. Click **Create** to start a new template.  
4. Navigate through the sections (Study, Design, Hardware, Preprocessing, Measurement, Visualization, etc.) and fill in the relevant fields.  
5. Click **Save** to save progress.  
6. Use **My templates** to review or manage your templates (set visibility, export, delete).  
7. Templates can be exported:  
   - PDF (for human reading)  
   - JSON (machine-readable, for archival or integration)  
8. You can **upload** previously exported templates (JSON) to your account.  

### Local Development (for Contributors)

> *These instructions assume you’re contributing to the web app (frontend/backend).*

1. **Fork** this repository and clone it locally.  
2. Install required dependencies (check `requirements.txt`, `mkdocs.yml`, etc.).  
3. Start the development server.  
4. Explore the template logic, UI, export modules (PDF/JSON).  
5. Implement or test your changes locally.  
6. Commit and push to your fork.  
7. Open a **Pull Request** to propose your changes.  

Refer to **CONTRIBUTING.md** for more detailed instructions, style guidelines, and governance.

## Project Structure

```text
.
├── .github/                 # GitHub workflows, issue templates, etc.
├── convert_table/           # scripts or modules for table conversions
├── inputs/                   # definition of input schemas or templates
├── outputs/                  # example outputs (PDF, JSON)
├── schemas/ artemis/         # JSON schema definitions for templates
├── src/                      # main source code (frontend, backend)
├── mkdocs.yml                # documentation / site configuration
├── requirements.txt          # Python dependencies
├── LICENSE                   # CC-BY 4.0 license
└── README.md                 # this file
```
## 🧩 Contributing

We welcome contributions of all kinds — **code, documentation, UX improvements, examples, and community outreach**.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for details on:

- How to raise issues  
- Coding conventions  
- Branching / PR workflow  
- Style guidelines  
- Governance and code of conduct  

### 💡 Starting Ideas
- Clarify or refine ambiguous template questions  
- Add hardware or preprocessing options (e.g., new EEG system, filter type)  
- Improve UI (labels, tooltips, validation)  
- Expand export functionality  
- Add example templates or case studies  
- Translate to other languages  

---

## 📚 Citation & Licensing

If you use **ARTEM-IS** in your work, kindly cite:

> Ković, V., et al. *“ARTEM-IS for ERP: Agreed Reporting Template for EEG Methodology.”* OSF, 2025.  
> [OSF Project Page](https://osf.io)

This project is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.  
[GitHub Repository](https://github.com/INCF/artem-is)

---

## 🚀 Roadmap & Future Directions

- Extend templates for **non-ERP EEG paradigms**  
- Support **mixed / multimodal experiments** (EEG + MEG, EEG + fMRI)  
- Enable **hierarchical / nested experimental designs**  
- Enhance **API / integration** with data repositories and analysis pipelines  
- Encourage **community-driven improvements, translations, and domain extensions**  

---

## 💬 Contact & Community

- Browse or submit issues: [GitHub Issues](https://github.com/INCF/artem-is/issues)  
- Join the community via [OSF](https://osf.io) or project mailing lists  
- Talks, slides, and related resources are available on the [ARTEM-IS OSF page](https://osf.io)

---

✨ **Thank you for your interest in improving transparency and rigor in EEG/ERP research!**  
We look forward to your contributions. 🎯
