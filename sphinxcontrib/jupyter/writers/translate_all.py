import re
import nbformat.v4
from .translate_code import JupyterCodeTranslator


class JupyterTranslator(JupyterCodeTranslator):
    SPLIT_URI_ID_REGEX = re.compile(r"([^\#]*)\#?(.*)")

    def __init__(self, builder, document):
        super().__init__(builder, document)

        # Settings
        self.sep_lines = "  \n"
        self.sep_paras = "\n\n"
        self.indent_char = " "
        self.indent = self.indent_char * 4
        self.default_ext = ".ipynb"

        # Variables used in visit/depart
        self.in_code_block = False  # if False, it means in markdown_cell
        self.code_lines = []

        self.markdown_lines = []

        self.indents = []
        self.section_level = 0
        self.bullets = []
        self.list_item_starts = []
        self.in_topic = False
        self.reference_text_start = 0
        self.in_reference = False
        self.list_level = 0
        self.in_citation = False

        self.table_builder = None

        fileName = document.settings._source.split("/")[-1].split(".")[0] + ".xmlDump"
        self.dumpFile = open("/home/nsifniotis/PycharmProjects/dumpfiles/" + fileName, "w")

    # specific visit and depart methods
    # ---------------------------------

    def visit_document(self, node):
        self.dumpFile.write("<document>\n")

    def depart_document(self, node):
        self.dumpFile.write("</document>\n")
        self.dumpFile.close()

    def visit_Text(self, node):
        self.dumpFile.write("<text>\n")

    def depart_Text(self, node):
        self.dumpFile.write("</text>\n")

    def visit_section(self, node):
        self.dumpFile.write("<section>\n")

    def depart_section(self, node):
        self.dumpFile.write("</section>\n")

    def visit_topic(self, node):
        self.dumpFile.write("<topic>\n")

    def depart_topic(self, node):
        self.dumpFile.write("</topic>\n")

    def visit_sidebar(self, node):
        self.dumpFile.write("<sidebar>\n")

    def depart_sidebar(self, node):
        self.dumpFile.write("</sidebar>\n")

    def visit_title(self, node):
        self.dumpFile.write("<title>\n")

    def depart_title(self, node):
        self.dumpFile.write("</title>\n")

    def visit_subtitle(self, node):
        self.dumpFile.write("<subtitle>\n")

    def depart_subtitle(self, node):
        self.dumpFile.write("</subtitle>\n")

    def visit_decoration(self, node):
        self.dumpFile.write("<decoration>\n")

    def depart_decoration(self, node):
        self.dumpFile.write("</decoration>\n")

    def visit_docinfo(self, node):
        self.dumpFile.write("<docinfo>\n")

    def depart_docinfo(self, node):
        self.dumpFile.write("</docinfo>\n")

    def visit_transition(self, node):
        self.dumpFile.write("<transition>\n")

    def depart_transition(self, node):
        self.dumpFile.write("</transition>\n")

    def visit_address(self, node):
        self.dumpFile.write("<address>\n")

    def depart_address(self, node):
        self.dumpFile.write("</address>\n")

    def visit_author(self, node):
        self.dumpFile.write("<author>\n")

    def depart_author(self, node):
        self.dumpFile.write("</author>\n")

    def visit_authors(self, node):
        self.dumpFile.write("<authors>\n")

    def depart_authors(self, node):
        self.dumpFile.write("</authors>\n")

    def visit_contact(self, node):
        self.dumpFile.write("<contact>\n")

    def depart_contact(self, node):
        self.dumpFile.write("</contact>\n")

    def visit_copyright(self, node):
        self.dumpFile.write("<copyright>\n")

    def depart_copyright(self, node):
        self.dumpFile.write("</copyright>\n")

    def visit_date(self, node):
        self.dumpFile.write("<date>\n")

    def depart_date(self, node):
        self.dumpFile.write("</date>\n")

    def visit_field(self, node):
        self.dumpFile.write("<field>\n")

    def depart_field(self, node):
        self.dumpFile.write("</field>\n")

    def visit_organization(self, node):
        self.dumpFile.write("<organization>\n")

    def depart_organization(self, node):
        self.dumpFile.write("</organization>\n")

    def visit_revision(self, node):
        self.dumpFile.write("<revision>\n")

    def depart_revision(self, node):
        self.dumpFile.write("</revision>\n")

    def visit_status(self, node):
        self.dumpFile.write("<status>\n")

    def depart_status(self, node):
        self.dumpFile.write("</status>\n")

    def visit_version(self, node):
        self.dumpFile.write("<version>\n")

    def depart_version(self, node):
        self.dumpFile.write("</version>\n")

    def visit_footer(self, node):
        self.dumpFile.write("<footer>\n")

    def depart_footer(self, node):
        self.dumpFile.write("</footer>\n")

    def visit_header(self, node):
        self.dumpFile.write("<header>\n")

    def depart_header(self, node):
        self.dumpFile.write("</header>\n")

    def visit_admonition(self, node):
        self.dumpFile.write("<admonition>\n")

    def depart_admonition(self, node):
        self.dumpFile.write("</admonition>\n")

    def visit_attention(self, node):
        self.dumpFile.write("<attention>\n")

    def depart_attention(self, node):
        self.dumpFile.write("</attention>\n")

    def visit_block_quote(self, node):
        self.dumpFile.write("<block_quote>\n")

    def depart_block_quote(self, node):
        self.dumpFile.write("</block_quote>\n")

    def visit_bullet_list(self, node):
        self.dumpFile.write("<bullet_list>\n")

    def depart_bullet_list(self, node):
        self.dumpFile.write("</bullet_list>\n")

    def visit_caution(self, node):
        self.dumpFile.write("<caution>\n")

    def depart_caution(self, node):
        self.dumpFile.write("</caution>\n")

    def visit_citation(self, node):
        self.dumpFile.write("<citation>\n")

    def depart_citation(self, node):
        self.dumpFile.write("</citation>\n")

    def visit_comment(self, node):
        self.dumpFile.write("<comment>\n")

    def depart_comment(self, node):
        self.dumpFile.write("</comment>\n")

    def visit_compound(self, node):
        self.dumpFile.write("<compound>\n")

    def depart_compound(self, node):
        self.dumpFile.write("</compound>\n")

    def visit_container(self, node):
        self.dumpFile.write("<container>\n")

    def depart_container(self, node):
        self.dumpFile.write("</container>\n")

    def visit_danger(self, node):
        self.dumpFile.write("<danger>\n")

    def depart_danger(self, node):
        self.dumpFile.write("</danger>\n")

    def visit_definition_list(self, node):
        self.dumpFile.write("<definition_list>\n")

    def depart_definition_list(self, node):
        self.dumpFile.write("</definition_list>\n")

    def visit_doctest_block(self, node):
        self.dumpFile.write("<doctest_block>\n")

    def depart_doctest_block(self, node):
        self.dumpFile.write("</doctest_block>\n")

    def visit_enumerated_list(self, node):
        self.dumpFile.write("<enumerated_list>\n")

    def depart_enumerated_list(self, node):
        self.dumpFile.write("</enumerated_list>\n")

    def visit_error(self, node):
        self.dumpFile.write("<error>\n")

    def depart_error(self, node):
        self.dumpFile.write("</error>\n")

    def visit_field_list(self, node):
        self.dumpFile.write("<field_list>\n")

    def depart_field_list(self, node):
        self.dumpFile.write("</field_list>\n")

    def visit_figure(self, node):
        self.dumpFile.write("<figure>\n")

    def depart_figure(self, node):
        self.dumpFile.write("</figure>\n")

    def visit_footnote(self, node):
        self.dumpFile.write("<footnote>\n")

    def depart_footnote(self, node):
        self.dumpFile.write("</footnote>\n")

    def visit_hint(self, node):
        self.dumpFile.write("<hint>\n")

    def depart_hint(self, node):
        self.dumpFile.write("</hint>\n")

    def visit_image(self, node):
        self.dumpFile.write("<image>\n")

    def depart_image(self, node):
        self.dumpFile.write("</image>\n")

    def visit_important(self, node):
        self.dumpFile.write("<important>\n")

    def depart_important(self, node):
        self.dumpFile.write("</important>\n")

    def visit_line_block(self, node):
        self.dumpFile.write("<line_block>\n")

    def depart_line_block(self, node):
        self.dumpFile.write("</line_block>\n")

    def visit_literal_block(self, node):
        self.dumpFile.write("<literal_block>\n")

    def depart_literal_block(self, node):
        self.dumpFile.write("</literal_block>\n")

    def visit_note(self, node):
        self.dumpFile.write("<note>\n")

    def depart_note(self, node):
        self.dumpFile.write("</note>\n")

    def visit_option_list(self, node):
        self.dumpFile.write("<option_list>\n")

    def depart_option_list(self, node):
        self.dumpFile.write("</option_list>\n")

    def visit_paragraph(self, node):
        self.dumpFile.write("<paragraph>\n")

    def depart_paragraph(self, node):
        self.dumpFile.write("</paragraph>\n")

    def visit_pending(self, node):
        self.dumpFile.write("<pending>\n")

    def depart_pending(self, node):
        self.dumpFile.write("</pending>\n")

    def visit_raw(self, node):
        self.dumpFile.write("<raw>\n")

    def depart_raw(self, node):
        self.dumpFile.write("</raw>\n")

    def visit_rubric(self, node):
        self.dumpFile.write("<rubric>\n")

    def depart_rubric(self, node):
        self.dumpFile.write("</rubric>\n")

    def visit_substitution_definition(self, node):
        self.dumpFile.write("<substitution_definition>\n")

    def depart_substitution_definition(self, node):
        self.dumpFile.write("</substitution_definition>\n")

    def visit_system_message(self, node):
        self.dumpFile.write("<system_message>\n")

    def depart_system_message(self, node):
        self.dumpFile.write("</system_message>\n")

    def visit_table(self, node):
        self.dumpFile.write("<table>\n")

    def depart_table(self, node):
        self.dumpFile.write("</table>\n")

    def visit_target(self, node):
        self.dumpFile.write("<target>\n")

    def depart_target(self, node):
        self.dumpFile.write("</target>\n")

    def visit_tip(self, node):
        self.dumpFile.write("<tip>\n")

    def depart_tip(self, node):
        self.dumpFile.write("</tip>\n")

    def visit_warning(self, node):
        self.dumpFile.write("<warning>\n")

    def depart_warning(self, node):
        self.dumpFile.write("</warning>\n")

    def visit_attribution(self, node):
        self.dumpFile.write("<attribution>\n")

    def depart_attribution(self, node):
        self.dumpFile.write("</attribution>\n")

    def visit_caption(self, node):
        self.dumpFile.write("<caption>\n")

    def depart_caption(self, node):
        self.dumpFile.write("</caption>\n")

    def visit_classifier(self, node):
        self.dumpFile.write("<classifier>\n")

    def depart_classifier(self, node):
        self.dumpFile.write("</classifier>\n")

    def visit_colspec(self, node):
        self.dumpFile.write("<colspec>\n")

    def depart_colspec(self, node):
        self.dumpFile.write("</colspec>\n")

    def visit_field_name(self, node):
        self.dumpFile.write("<field_name>\n")

    def depart_field_name(self, node):
        self.dumpFile.write("</field_name>\n")

    def visit_label(self, node):
        self.dumpFile.write("<label>\n")

    def depart_label(self, node):
        self.dumpFile.write("</label>\n")

    def visit_line(self, node):
        self.dumpFile.write("<line>\n")

    def depart_line(self, node):
        self.dumpFile.write("</line>\n")

    def visit_option_argument(self, node):
        self.dumpFile.write("<option_argument>\n")

    def depart_option_argument(self, node):
        self.dumpFile.write("</option_argument>\n")

    def visit_option_string(self, node):
        self.dumpFile.write("<option_string>\n")

    def depart_option_string(self, node):
        self.dumpFile.write("</option_string>\n")

    def visit_term(self, node):
        self.dumpFile.write("<term>\n")

    def depart_term(self, node):
        self.dumpFile.write("</term>\n")

    def visit_definition(self, node):
        self.dumpFile.write("<definition>\n")

    def depart_definition(self, node):
        self.dumpFile.write("</definition>\n")

    def visit_definition_list_item(self, node):
        self.dumpFile.write("<definition_list_item>\n")

    def depart_definition_list_item(self, node):
        self.dumpFile.write("</definition_list_item>\n")

    def visit_description(self, node):
        self.dumpFile.write("<description>\n")

    def depart_description(self, node):
        self.dumpFile.write("</description>\n")

    def visit_entry(self, node):
        self.dumpFile.write("<entry>\n")

    def depart_entry(self, node):
        self.dumpFile.write("</entry>\n")

    def visit_field(self, node):
        self.dumpFile.write("<field>\n")

    def depart_field(self, node):
        self.dumpFile.write("</field>\n")

    def visit_field_body(self, node):
        self.dumpFile.write("<field_body>\n")

    def depart_field_body(self, node):
        self.dumpFile.write("</field_body>\n")

    def visit_legend(self, node):
        self.dumpFile.write("<legend>\n")

    def depart_legend(self, node):
        self.dumpFile.write("</legend>\n")

    def visit_list_item(self, node):
        self.dumpFile.write("<list_item>\n")

    def depart_list_item(self, node):
        self.dumpFile.write("</list_item>\n")

    def visit_option(self, node):
        self.dumpFile.write("<option>\n")

    def depart_option(self, node):
        self.dumpFile.write("</option>\n")

    def visit_option_group(self, node):
        self.dumpFile.write("<option_group>\n")

    def depart_option_group(self, node):
        self.dumpFile.write("</option_group>\n")

    def visit_option_list_item(self, node):
        self.dumpFile.write("<option_list_item>\n")

    def depart_option_list_item(self, node):
        self.dumpFile.write("</option_list_item>\n")

    def visit_row(self, node):
        self.dumpFile.write("<row>\n")

    def depart_row(self, node):
        self.dumpFile.write("</row>\n")

    def visit_tbody(self, node):
        self.dumpFile.write("<tbody>\n")

    def depart_tbody(self, node):
        self.dumpFile.write("</tbody>\n")

    def visit_tgroup(self, node):
        self.dumpFile.write("<tgroup>\n")

    def depart_tgroup(self, node):
        self.dumpFile.write("</tgroup>\n")

    def visit_thead(self, node):
        self.dumpFile.write("<thead>\n")

    def depart_thead(self, node):
        self.dumpFile.write("</thead>\n")

    def visit_abbreviation(self, node):
        self.dumpFile.write("<abbreviation>\n")

    def depart_abbreviation(self, node):
        self.dumpFile.write("</abbreviation>\n")

    def visit_acronym(self, node):
        self.dumpFile.write("<acronym>\n")

    def depart_acronym(self, node):
        self.dumpFile.write("</acronym>\n")

    def visit_citation_reference(self, node):
        self.dumpFile.write("<citation_reference>\n")

    def depart_citation_reference(self, node):
        self.dumpFile.write("</citation_reference>\n")

    def visit_emphasis(self, node):
        self.dumpFile.write("<emphasis>\n")

    def depart_emphasis(self, node):
        self.dumpFile.write("</emphasis>\n")

    def visit_footnote_reference(self, node):
        self.dumpFile.write("<footnote_reference>\n")

    def depart_footnote_reference(self, node):
        self.dumpFile.write("</footnote_reference>\n")

    def visit_generated(self, node):
        self.dumpFile.write("<generated>\n")

    def depart_generated(self, node):
        self.dumpFile.write("</generated>\n")

    def visit_image(self, node):
        self.dumpFile.write("<image>\n")

    def depart_image(self, node):
        self.dumpFile.write("</image>\n")

    def visit_inline(self, node):
        self.dumpFile.write("<inline>\n")

    def depart_inline(self, node):
        self.dumpFile.write("</inline>\n")

    def visit_literal(self, node):
        self.dumpFile.write("<literal>\n")

    def depart_literal(self, node):
        self.dumpFile.write("</literal>\n")

    def visit_math(self, node):
        self.dumpFile.write("<math>\n")

    def depart_math(self, node):
        self.dumpFile.write("</math>\n")

    def visit_problematic(self, node):
        self.dumpFile.write("<problematic>\n")

    def depart_problematic(self, node):
        self.dumpFile.write("</problematic>\n")

    def visit_reference(self, node):
        self.dumpFile.write("<reference>\n")

    def depart_reference(self, node):
        self.dumpFile.write("</reference>\n")

    def visit_strong(self, node):
        self.dumpFile.write("<strong>\n")

    def depart_strong(self, node):
        self.dumpFile.write("</strong>\n")

    def visit_subscript(self, node):
        self.dumpFile.write("<subscript>\n")

    def depart_subscript(self, node):
        self.dumpFile.write("</subscript>\n")

    def visit_substitution_reference(self, node):
        self.dumpFile.write("<substitution_reference>\n")

    def depart_substitution_reference(self, node):
        self.dumpFile.write("</substitution_reference>\n")

    def visit_superscript(self, node):
        self.dumpFile.write("<superscript>\n")

    def depart_superscript(self, node):
        self.dumpFile.write("</superscript>\n")

    def visit_target(self, node):
        self.dumpFile.write("<target>\n")

    def depart_target(self, node):
        self.dumpFile.write("</target>\n")

    def visit_title_reference(self, node):
        self.dumpFile.write("<title_reference>\n")

    def depart_title_reference(self, node):
        self.dumpFile.write("</title_reference>\n")

    def visit_raw(self, node):
        self.dumpFile.write("<raw>\n")

    def depart_raw(self, node):
        self.dumpFile.write("</raw>\n")


    # ===================
    #  general methods
    # ===================
    def add_markdown_cell(self):
        """split a markdown cell here

        * append `markdown_lines` to notebook
        * reset `markdown_lines`
        """
        line_text = "".join(self.markdown_lines)
        formatted_line_text = self.strip_blank_lines_in_end_of_block(line_text)

        if len(formatted_line_text.strip()) > 0:
            new_md_cell = nbformat.v4.new_markdown_cell(formatted_line_text)
            self.output["cells"].append(new_md_cell)
            self.markdown_lines = []

    @classmethod
    def split_uri_id(cls, uri):
        return re.search(cls.SPLIT_URI_ID_REGEX, uri).groups()

    @classmethod
    def add_extension_to_inline_link(cls, uri, ext):
        if "." not in uri:
            uri, id_ = cls.split_uri_id(uri)
            return "{}{}#{}".format(uri, ext, id_)

        return uri

