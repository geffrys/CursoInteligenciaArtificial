import { Component, OnInit } from '@angular/core';
import { MusicExpertServiceService } from '../../services/music-expert-service.service';

@Component({
  selector: 'app-music-expert-system-form',
  templateUrl: './music-expert-system-form.component.html',
  styleUrls: ['./music-expert-system-form.component.css']
})
export class MusicExpertSystemFormComponent implements OnInit {

  recomendations: any[] = [];
  moods: [] = [];
  genres: [] = [];

  constructor(private musicExpert: MusicExpertServiceService) { }

  onSubmit(personForm: any): void {
    console.log(personForm);
    this.musicExpert.evaluate(personForm.value).subscribe((data: any) => {
      this.recomendations = data.map((e: any) => e.fact_conditions);
      console.log(this.recomendations);
      console.log(data);
    } , );
  }

  ngOnInit(): void {
    this.musicExpert.getMoods().forEach((data: any) => {
      this.moods = data.moods;
    }, );
    this.musicExpert.getGenres().forEach((data: any) => {
      this.genres = data.genres;
    }, );
  }

}
