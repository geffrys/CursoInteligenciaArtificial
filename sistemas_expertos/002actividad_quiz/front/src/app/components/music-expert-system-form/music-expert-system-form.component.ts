import { Component, OnInit } from '@angular/core';
import { MusicExpertServiceService } from '../../services/music-expert-service.service';

@Component({
  selector: 'app-music-expert-system-form',
  templateUrl: './music-expert-system-form.component.html',
  styleUrls: ['./music-expert-system-form.component.css']
})
export class MusicExpertSystemFormComponent implements OnInit {

  moods: [] = [];

  constructor(private musicExpert: MusicExpertServiceService) { }

  onSubmit(personForm: any): void {
    console.log(personForm);
  }

  ngOnInit(): void {
    this.musicExpert.getMoods().forEach((data: any) => {
      this.moods = data.moods;
    }, );
  }

}
