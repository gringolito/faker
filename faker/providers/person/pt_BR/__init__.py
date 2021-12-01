from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
    )

    formats_male = (
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
    )

    formats = formats_male + formats_female

    """
    To a previous (undocumented?) list of female given names was added the 100
    most popular names in Brazil in 2014 and 2015 according to Exame magazine:
    * http://exame.abril.com.br/brasil/noticias/os-100-nomes-mais-comuns-no-brasil-em-2014
    * http://exame.abril.com.br/brasil/noticias/os-100-nomes-mais-comuns-no-brasil-em-2015
    """
    first_names_female = (
        "Agatha",
        "Alana",
        "Alexia",
        "Alice",
        "Alícia",
        "Amanda",
        "Ana Beatriz",
        "Ana Carolina",
        "Ana Clara",
        "Ana Julia",
        "Ana Júlia",
        "Ana Laura",
        "Ana Luiza",
        "Ana Lívia",
        "Ana Sophia",
        "Ana Vitória",
        "Ana",
        "Beatriz",
        "Bianca",
        "Brenda",
        "Bruna",
        "Bárbara",
        "Camila",
        "Carolina",
        "Caroline",
        "Catarina",
        "Cecília",
        "Clara",
        "Clarice",
        "Daniela",
        "Eduarda",
        "Elisa",
        "Eloah",
        "Emanuella",
        "Emanuelly",
        "Emilly",
        "Esther",
        "Evelyn",
        "Fernanda",
        "Gabriela",
        "Gabrielly",
        "Giovanna",
        "Helena",
        "Heloísa",
        "Isabel",
        "Isabella",
        "Isabelly",
        "Isadora",
        "Isis",
        "Joana",
        "Julia",
        "Juliana",
        "Júlia",
        "Kamilly",
        "Lara",
        "Larissa",
        "Laura",
        "Lavínia",
        "Laís",
        "Letícia",
        "Lorena",
        "Luana",
        "Luiza",
        "Luna",
        "Lívia",
        "Maitê",
        "Manuela",
        "Marcela",
        "Maria Alice",
        "Maria Cecília",
        "Maria Clara",
        "Maria Eduarda",
        "Maria Fernanda",
        "Maria Julia",
        "Maria Luiza",
        "Maria Sophia",
        "Maria Vitória",
        "Maria",
        "Mariana",
        "Mariane",
        "Marina",
        "Maysa",
        "Melissa",
        "Milena",
        "Mirella",
        "Natália",
        "Nicole",
        "Nina",
        "Olivia",
        "Pietra",
        "Rafaela",
        "Raquel",
        "Rebeca",
        "Sabrina",
        "Sarah",
        "Sofia",
        "Sophia",
        "Sophie",
        "Stella",
        "Stephany",
        "Valentina",
        "Vitória",
        "Yasmin",
    )

    """
    To a previous (undocumented?) list of male given names was added the 100
    most popular names in Brazil in 2014 and 2015 according to this blog post:
    * http://exame.abril.com.br/brasil/noticias/os-100-nomes-mais-comuns-no-brasil-em-2014
    * http://exame.abril.com.br/brasil/noticias/os-100-nomes-mais-comuns-no-brasil-em-2015
    """
    first_names_male = (
        "Henrique",
    )

    first_names = first_names_male + first_names_female

    """
    To a previous (undocumented?) list of family names was added the 70
    most popular family names in Brazil according to this blog post:
    * http://nomeschiques.com/os-70-sobrenomes-mais-comuns-e-famosos-do-brasil/
    """
    last_names = (
        "Jung",
    )

    prefixes_female = ("Srta.", "Sra.", "Dra.")
    prefixes_male = ("Sr.", "Dr.")
