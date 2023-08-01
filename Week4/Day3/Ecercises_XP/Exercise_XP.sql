--EXERCISE 1:

--select language.name
-- from language;

-- select film.title, description, language.name
-- from film
-- join language
-- on film.language_id = language.language_id;

-- SELECT film.title, description, language.name
-- FROM public.film
-- WHERE language_id IS NULL

-- select film.title, description, language.name
-- from film
-- FULL outer join language
-- on film.language_id = language.language_id; 

-- create table new_film(
-- id serial primary key,
-- name varchar(50) );

-- insert into new_film(name) 
-- values
--    ('Titanic Matt Damon'),
--    ('Garry Potter Iron Man'),
--    ('Interstellar')
   
-- create table customer_review(
-- review_id serial primary key,
-- 	film_id int references new_film (id),
-- 	language_id int references language (language_id),
-- 	title varchar(50) not null,
-- 	score int check(score between 1 and 10) not null,
-- 	review_text text not null,
-- 	last_update date not null
-- 	)
	
-- insert into customer_review (film_id, language_id, title, score, review_text, last_update) 
-- values
-- ((select id from new_film where name ilike 't%'), (select language_id from language where name = 'Japanese'), '史上最高の言語', 8, 'この映画は私の子供時代のお気に入りの 1 つです。この映画が公開されたとき、私はまだ 7 ～ 8 歳で、現代のテクノロジーである YouTube が存在しなかった頃、ビデオにロードされてよく見ていました。 100回目の記念に母と私は3Dで観て、最近公開されてから25周年ということで一緒にもう一度観ましたが、とても壮大なので100回以上観てもいいような気がします。 特にジャック・ローズが浸水した甲板に閉じ込められ、最後に脱出する場面や、船がベニドルムの超高層ビルのように上昇し、乗客全員が苦痛の叫び声を上げ、互いにぶつかり合い、その後ローズ・ジャックの顔を見る場面は、文字通り船に乗っているような気分になります。 彼らの呼吸は、特にローズが「ああ、なんてことだ」と3回も言ったときに、彼らの中にある恐怖を大いに感じることができ、私の心臓は高鳴り、手は熱くて汗ばみました。 最後の素晴らしい部分は、モリーが知人に戻るよう勧め、警官に彼女の心の一部を与え、彼がそれを彼女に返したときです。 私のお気に入りのシーンは、ジャックがファーストクラスの乗客と夕食をとっているネズミはほとんどいないと言うところ、モリー・ブラウンが誰かが火をつけるとジャックに「あなたは新しいペニーのように輝く、とても素敵な瞬間です」と言っているところです。 さて、これらのシーンは、ローズがジャックを助けようとしてカルの顔に唾を吐き、その男の顔を殴り、ローズがドアを破壊して執事に「黙れ」と叫ぶシーンで、常に映画館の観客を縫合します。 心を掴むような悲しいシーンがあるのは、
--   ローズ・ジャックがあの少年とその父親を助け出そうとするが、その後みんな流されて大階段も歌とともに沈む 偉大な故ジェームス・ホーナーのビルディング・パニック 文字通りアッセンジャーの叫び声は本当に骨が凍るような胸の張り裂ける音だ
-- 逃げ場もなく、窓が全部潰れてドームが爆発するシーンは本当に衝撃的でした。 映画館の従業員も 1 人か 2 人で、『オールド・ローズ』の最後の瞬間だけでなく、『船』の最後の瞬間も観に来ますが、特にオールド・ローズがネックレスを海に投げ捨てる最後は、とても古典的な悲痛な映画なので、良い雰囲気を与えてくれます。 それから、「人生が大きく変わった」という曲で、私は本当に泣きました、そしておそらく映画館全体がこの曲で彼女が当時経験したことを反映しているので、ジャックが彼女にたくさんの子供たちに世界を旅行させるつもりだと言ったときのような良い人生さえも反映していました。 そして死ぬ
--   暖かく快適なベッドでローズのテーマが流れ、彼女が静かに去っていくとき、私の目は涙を流しましたが、それはただ悲しい美しい結末で止まりました。', '2023-01-01' ),
--  ((select id from new_film where name ilike 'g%'), (select language_id from language where name ilike 'i%'), 'La serie di Harry Potter', 10, 'La serie di Harry Potter, scritta da J.K. Rowling, ha senza dubbio conquistato i cuori e limmaginazione di milioni di lettori in tutto il mondo. Con la sua incantevole miscela di magia, amicizia e avventura, questa saga di sette libri è diventata un fenomeno letterario moderno. Fin dal primo libro, "Harry Potter e la pietra filosofale" (o "Pietra filosofale" negli Stati Uniti), i lettori vengono introdotti in un mondo di meraviglia ed eccitazione. La storia segue il giovane mago, Harry Potter, come scopre la sua eredità magica e si iscrive alla Scuola di Magia e Stregoneria di Hogwarts.La narrazione fantasiosa di Rowling attira immediatamente i lettori in un regno in cui creature mitiche, incantesimi e partite di Quidditch fanno parte della vita di tutti i giorni.Uno dei maggiori punti di forza della serie risiede nei suoi personaggi. Harry Potter, Hermione Granger e Ron Weasley diventano rapidamente figure amate e i lettori si ritrovano a fare il tifo per loro mentre affrontano varie sfide e ostacoli durante il loro viaggio.Lo sviluppo del personaggio di Rowling è eccezionale, consentendo ai lettori di assistere alla crescita e alla maturazione di questi personaggi nel corso il corso della serie. Inoltre, le trame intricate e i misteri accuratamente intrecciati rendono ogni libro un libro che gira pagina. Dalle stanze nascoste di Hogwarts alla battaglia contro il Signore Oscuro, Voldemort, Rowling crea sapientemente una narrazione che tiene i lettori al limite dei loro posti. Il ritmo della storia è ben bilanciato, con momenti di leggerezza e umorismo intervallati
--   azione intensa e profondità emotiva. Oltre alla sua trama accattivante, la serie di Harry Potter affronta anche temi importanti come lamore, il sacrificio, il pregiudizio e il potere delamicizia. Rowling integra perfettamente questi temi nella narrazione, incoraggiando i lettori a riflettere sulle complessità del mondo che li circonda. I libri offrono preziose lezioni di vita che si estendono
--   oltre il regno della magia, rendendoli riconoscibili e di grande impatto per i lettori di tutte le età. Inoltre, la ricca costruzione del mondo di Rowling non lascia alcun dettaglio inesplorato. Da Diagon Alley a Hogwarts
--   scale mobili, le vivide descrizioni consentono ai lettori di visualizzare ogni aspetto del mondo magico. La capacità della Rowling di creare un ambiente così coinvolgente aggiunge un altro livello
--   di incanto allesperienza di lettura. Tuttavia, vale la pena ricordare che la serie diventa progressivamente più oscura e matura man mano che procede. I libri successivi trattano temi complessi e cupi, che potrebbero non essere adatti a lettori molto giovani. È importante che genitori e tutori considerino ladeguatezza alletà di ciascun libro. In conclusione, la serie di Harry Potter è un risultato straordinario in letteratura. J.K. Il mondo magico e i personaggi indimenticabili della Rowling hanno lasciato un segno indelebile nella letteratura contemporanea e il suo impatto sulla cultura popolare è innegabile. Che tu sia un giovane lettore che scopre i libri per la prima volta o un adulto che rivisita la serie, il viaggio attraverso il mondo di Harry Potter è unesperienza affascinante e trasformativa che senza dubbio lascerà unimpressione duratura.',  '2022-01-01')
 
-- ALTER TABLE public.customer_review
-- DROP CONSTRAINT customer_review_film_id_fkey,
-- ADD CONSTRAINT customer_review_film_id_fkey
--   FOREIGN KEY (film_id)
--   REFERENCES new_film (id)
--   ON DELETE CASCADE
--   ON UPDATE CASCADE;
  
-- ALTER TABLE public.customer_review
-- DROP CONSTRAINT customer_review_language_id_fkey,
-- ADD CONSTRAINT customer_review_language_id_fkey
--   FOREIGN KEY (language_id)
--   REFERENCES language (language_id)
--   ON DELETE CASCADE
--   ON UPDATE CASCADE;

-- select * from new_film;

-- delete from new_film
-- where name ilike 'g%';

-- insert into customer_review (film_id, language_id, title, score, review_text, last_update) 
-- values
-- ((select id from new_film where name ilike 'g%'), (select language_id from language where name ilike 'i%'), 'La serie di Harry Potter', 10, 'La serie di Harry Potter, scritta da J.K. Rowling, ha senza dubbio conquistato i cuori e limmaginazione di milioni di lettori in tutto il mondo. Con la sua incantevole miscela di magia, amicizia e avventura, questa saga di sette libri è diventata un fenomeno letterario moderno. Fin dal primo libro, "Harry Potter e la pietra filosofale" (o "Pietra filosofale" negli Stati Uniti), i lettori vengono introdotti in un mondo di meraviglia ed eccitazione. La storia segue il giovane mago, Harry Potter, come scopre la sua eredità magica e si iscrive alla Scuola di Magia e Stregoneria di Hogwarts.La narrazione fantasiosa di Rowling attira immediatamente i lettori in un regno in cui creature mitiche, incantesimi e partite di Quidditch fanno parte della vita di tutti i giorni.Uno dei maggiori punti di forza della serie risiede nei suoi personaggi. Harry Potter, Hermione Granger e Ron Weasley diventano rapidamente figure amate e i lettori si ritrovano a fare il tifo per loro mentre affrontano varie sfide e ostacoli durante il loro viaggio.Lo sviluppo del personaggio di Rowling è eccezionale, consentendo ai lettori di assistere alla crescita e alla maturazione di questi personaggi nel corso il corso della serie. Inoltre, le trame intricate e i misteri accuratamente intrecciati rendono ogni libro un libro che gira pagina. Dalle stanze nascoste di Hogwarts alla battaglia contro il Signore Oscuro, Voldemort, Rowling crea sapientemente una narrazione che tiene i lettori al limite dei loro posti. Il ritmo della storia è ben bilanciato, con momenti di leggerezza e umorismo intervallati
--    azione intensa e profondità emotiva. Oltre alla sua trama accattivante, la serie di Harry Potter affronta anche temi importanti come lamore, il sacrificio, il pregiudizio e il potere delamicizia. Rowling integra perfettamente questi temi nella narrazione, incoraggiando i lettori a riflettere sulle complessità del mondo che li circonda. I libri offrono preziose lezioni di vita che si estendono
--    oltre il regno della magia, rendendoli riconoscibili e di grande impatto per i lettori di tutte le età. Inoltre, la ricca costruzione del mondo di Rowling non lascia alcun dettaglio inesplorato. Da Diagon Alley a Hogwarts
--    scale mobili, le vivide descrizioni consentono ai lettori di visualizzare ogni aspetto del mondo magico. La capacità della Rowling di creare un ambiente così coinvolgente aggiunge un altro livello
--    di incanto allesperienza di lettura. Tuttavia, vale la pena ricordare che la serie diventa progressivamente più oscura e matura man mano che procede. I libri successivi trattano temi complessi e cupi, che potrebbero non essere adatti a lettori molto giovani. È importante che genitori e tutori considerino ladeguatezza alletà di ciascun libro. In conclusione, la serie di Harry Potter è un risultato straordinario in letteratura. J.K. Il mondo magico e i personaggi indimenticabili della Rowling hanno lasciato un segno indelebile nella letteratura contemporanea e il suo impatto sulla cultura popolare è innegabile. Che tu sia un giovane lettore che scopre i libri per la prima volta o un adulto che rivisita la serie, il viaggio attraverso il mondo di Harry Potter è unesperienza affascinante e trasformativa che senza dubbio lascerà unimpressione duratura.',  '2022-01-01')

-- insert into new_film(name) 
-- values
--   ('Titanic Matt Damon'),
--   ('Garry Potter Iron Man'),
--   ('Interstellar')
	
-- delete from new_film
-- using customer_review
-- where customer_review.film_id = (select id from new_film where new_film.name ilike 'g%');

-- delete from new_film
-- using customer_review
-- where customer_review.film_id = new_film.id
-- RETURNING *

-- EXERCISE 2:
--1.
-- update film
-- set language_id = 3
-- where title ilike '% _a%';

-- 2. customer_address_id_fkey, insert values into table like usual, but address_id in customer table need to be equal to address_pkey in address table

-- 3. drop table if exists customer_review; it was easy

-- 4. select count(rental_date) from rental
-- where return_date is null;

-- 5. select film.title, film.replacement_cost, rent.return_date 
-- from film
-- inner join inventory inv on inv.film_id = film.film_id
-- inner join rental rent on rent.inventory_id = inv.inventory_id
-- where rent.return_date is null
-- order by replacement_cost desc limit 30;

-- 6.1
-- select film.title, concat(a.first_name, ' ', a.last_name) actor
-- from film
-- inner join film_actor fa on fa.film_id = film.film_id
-- inner join actor a on a.actor_id = fa.actor_id
-- where film.description ilike '%sumo%'
-- and film.description ilike '%wrestler%'
-- and a.first_name ilike 'penelope'
-- and a.last_name ilike 'monroe';

-- 6.2
-- select film.title, film.rating, film.length
-- from film
-- inner join film_category fc on film.film_id = fc.film_id
-- inner join category c on c.category_id = fc.category_id
-- where film.rating = 'R' and film.length < 60;

--6.3
-- select film.title, concat(c.first_name, ' ', c.last_name), r.return_date, p.amount
-- from film
-- inner join inventory i on film.film_id = i.film_id
-- inner join rental r on r.inventory_id = i.inventory_id
-- inner join customer c on r.customer_id = c.customer_id
-- inner join payment p on r.rental_id = p.rental_id
-- where c.first_name ilike 'matthew'
-- and c.last_name ilike 'mahan'
-- and r.return_date between '2005-07-28' and '2005-08-01'
-- and p.amount > 4.00

--6.4

with max_replacement_cost_cte as (
  select max(f.replacement_cost) as max_replacement_cost
  from film f
  inner join inventory i on f.film_id = i.film_id
  inner join rental r on r.inventory_id = i.inventory_id
  inner join customer c on r.customer_id = c.customer_id
  where c.first_name ilike 'matthew'
    and c.last_name ilike 'mahan'
    and (f.description ilike '%boat%' or f.title ilike '%boat%')
)
select film.title, CONCAT(c.first_name, ' ', c.last_name) as customer, film.replacement_cost
from film
inner join inventory i on film.film_id = i.film_id
inner join rental r on r.inventory_id = i.inventory_id
inner join customer c on r.customer_id = c.customer_id
inner join max_replacement_cost_cte max_cost on film.replacement_cost = max_cost.max_replacement_cost
where c.first_name ilike 'matthew'
  and c.last_name ilike 'mahan'
  and (film.description ilike '%boat%' or film.title ilike '%boat%');
	  

-- select max(replacement_cost) from film;