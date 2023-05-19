lexer grammar DocBookGrammar;

docbook: (ARTICLE | BOOK | SECTION)+;

ARTICLE: OPEN_ARTICLE info? CONTENT CLOSE_ARTICLE;

BOOK: OPEN_BOOK info? CONTENT CLOSE_BOOK;

SECTION: OPEN_SECTION info? CONTENT CLOSE_SECTION;

CONTENT: (TITLE | PARA | ORDEREDLIST | UNORDEREDLIST | IMPORTANT | TABLE | FIGURE | CODE | NOTE)+;

info: (TITLE | AUTHOR | ABSTRACT | DATE | COPYRIGHT | ADDRESS);

TITLE: OPEN_TITLE TEXT CLOSE_TITLE;

AUTHOR: OPEN_AUTHOR TEXT CLOSE_AUTHOR;

ABSTRACT: OPEN_ABSTRACT TEXT CLOSE_ABSTRACT;

DATE: OPEN_DATE TEXT CLOSE_DATE;

COPYRIGHT: OPEN_COPYRIGHT TEXT CLOSE_COPYRIGHT;

ADDRESS: OPEN_ADDRESS TEXT CLOSE_ADDRESS;

PARA: OPEN_PARA TEXT CLOSE_PARA;

ORDEREDLIST: OPEN_ORDEREDLIST listItem+ CLOSE_ORDEREDLIST;

UNORDEREDLIST: OPEN_UNORDEREDLIST listItem+ CLOSE_UNORDEREDLIST;

listItem: OPEN_LISTITEM CONTENT CLOSE_LISTITEM;

IMPORTANT: OPEN_IMPORTANT CONTENT CLOSE_IMPORTANT;

TABLE: OPEN_TABLE TABLECONTENT CLOSE_TABLE;

TABLECONTENT: (TITLE | TABLEROW)+;

TABLEROW: OPEN_ROW TABLECELL+ CLOSE_ROW;

TABLECELL: OPEN_ENTRY TEXT CLOSE_ENTRY;

FIGURE: OPEN_FIGURE FIGURECONTENT CLOSE_FIGURE;

FIGURECONTENT: (TITLE | IMAGE);

IMAGE: OPEN_MEDIAOBJECT OPEN_IMAGEOBJECT OPEN_IMAGEDATA TEXT CLOSE_IMAGEDATA CLOSE_IMAGEOBJECT CLOSE_MEDIAOBJECT;

CODE: OPEN_PROGRAMLISTING TEXT CLOSE_PROGRAMLISTING;

NOTE: OPEN_NOTE CONTENT CLOSE_NOTE;

OPEN_ARTICLE: '<article>';
CLOSE_ARTICLE: '</article>';

OPEN_BOOK: '<book>';
CLOSE_BOOK: '</book>';

OPEN_SECTION: '<section>';
CLOSE_SECTION: '</section>';

OPEN_TITLE: '<title>';
CLOSE_TITLE: '</title>';

OPEN_AUTHOR: '<author>';
CLOSE_AUTHOR: '</author>';

OPEN_ABSTRACT: '<abstract>';
CLOSE_ABSTRACT: '</abstract>';

OPEN_DATE: '<date>';
CLOSE_DATE: '</date>';

OPEN_COPYRIGHT: '<copyright>';
CLOSE_COPYRIGHT: '</copyright>';

OPEN_ADDRESS: '<address>';
CLOSE_ADDRESS: '</address>';

OPEN_PARA: '<para>';
CLOSE_PARA: '</para>';

OPEN_ORDEREDLIST: '<orderedlist>';
CLOSE_ORDEREDLIST: '</orderedlist>';

OPEN_UNORDEREDLIST: '<itemizedlist>';
CLOSE_UNORDEREDLIST: '</itemizedlist>';

OPEN_LISTITEM: '<listitem>';
CLOSE_LISTITEM: '</listitem>';

OPEN_IMPORTANT: '<important>';
CLOSE_IMPORTANT: '</important>';

OPEN_TABLE: '<table>';
CLOSE_TABLE: '</table>';

OPEN_ROW: '<row>';
CLOSE_ROW: '</row>';

OPEN_ENTRY: '<entry>';
CLOSE_ENTRY: '</entry>';

OPEN_FIGURE: '<figure>';
CLOSE_FIGURE: '</figure>';

OPEN_MEDIAOBJECT: '<mediaobject>';
CLOSE_MEDIAOBJECT: '</mediaobject>';

OPEN_IMAGEOBJECT: '<imageobject>';
CLOSE_IMAGEOBJECT: '</imageobject>';

OPEN_IMAGEDATA: '<imagedata>';
CLOSE_IMAGEDATA: '</imagedata>';

OPEN_PROGRAMLISTING: '<programlisting>';
CLOSE_PROGRAMLISTING: '</programlisting>';

OPEN_NOTE: '<note>';
CLOSE_NOTE: '</note>';

TEXT: ~[<>]+;
